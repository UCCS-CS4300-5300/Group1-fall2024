import json
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe
from django.contrib import messages
import inflect
from django.http import JsonResponse
from django.views import View
from django.db.models import Q, Count
from django.db.models import Case, When, Value, IntegerField

from .models import Ingredient, Recipe, UserPreference, FavoriteRecipe, Diets, Rating, RecipeIngredient
from .forms import CreateUserForm, RecipeForm, RecipeIngredientForm
from .decorators import unauthenticated_user
from django.db import IntegrityError  # Import IntegrityError to handle database constraints
import uuid
from django.forms import modelformset_factory


def index(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = Ingredient.objects.annotate(
        recipe_count=Count('recipeingredient')
    ).order_by('-recipe_count')[:10]

    diets = Diets.objects.annotate(diet_count=Count('name')).order_by('-diet_count')

    # Create a dictionary of diet names and their respective blacklisted ingredients
    diet_blacklists = {
        diet.name: list(diet.blacklist.values_list('name', flat=True))
        for diet in diets
    }

    context = {
        'common_ingredients': common_ingredients,
        'diets': diets,
        'diet_blacklists': mark_safe(json.dumps(diet_blacklists)),  # Convert to JSON for JavaScript access
    }
    return render(request, 'cookapp/index.html', context)

def logout_message(request):
    return render(request, 'registration/logout.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().username}!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            user.save()

            messages.success(request, f'Welcome, {username}!')
            return redirect('index')  # Redirect to the home page
    context = {'form': form}
    return render(request, 'registration/register.html', context)

from django.db.models import Count

class RecipeSearch(View):
    def get(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('whitelist', '[]')
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 10))

        try:
            blacklist = json.loads(blacklist_query)
            whitelist = json.loads(whitelist_query)
        except json.JSONDecodeError:
            blacklist = []
            whitelist = []

        # Initialize the inflect engine
        p = inflect.engine()

        # Initialize the query
        if query:
            recipe_results = Recipe.objects.filter(
                Q(title__icontains=query) | Q(tags__icontains=query)
            )
        else:
            recipe_results = Recipe.objects.all()

        # Apply whitelist filter (include only recipes containing all specified whitelist ingredients)
        if whitelist:
            for ingredient in whitelist:
                try:
                    whitelisted_ingredients = Ingredient.objects.filter(name__icontains=ingredient).distinct()
                    if whitelisted_ingredients.exists():
                        recipe_results = recipe_results.filter(recipeingredient__ingredient__in=whitelisted_ingredients)
                    else:
                        # Try singular form
                        singular_ingredient = p.singular_noun(ingredient)
                        if singular_ingredient:
                            whitelisted_ingredients = Ingredient.objects.filter(name__icontains=singular_ingredient).distinct()
                            if whitelisted_ingredients.exists():
                                recipe_results = recipe_results.filter(recipeingredient__ingredient__in=whitelisted_ingredients)
                            else:
                                # If any ingredient in the whitelist is not found, no recipes can match
                                return JsonResponse({
                                    'recipes': [],
                                })
                        else:
                            # If any ingredient in the whitelist is not found, no recipes can match
                            return JsonResponse({
                                'recipes': [],
                            })
                except Ingredient.DoesNotExist:
                    # If any ingredient in the whitelist is not found, no recipes can match
                    return JsonResponse({'recipes': []})

        # Apply blacklist filter
        for ingredient in blacklist:
            try:
                blacklisted_ingredients = Ingredient.objects.filter(name__icontains=ingredient).distinct()
                if blacklisted_ingredients.exists():
                    recipe_results = recipe_results.exclude(recipeingredient__ingredient__in=blacklisted_ingredients)
                else:
                    # Try singular form
                    singular_ingredient = p.singular_noun(ingredient)
                    if singular_ingredient:
                        blacklisted_ingredients = Ingredient.objects.filter(name__icontains=singular_ingredient).distinct()
                        if blacklisted_ingredients.exists():
                            recipe_results = recipe_results.exclude(recipeingredient__ingredient__in=blacklisted_ingredients)
                        else:
                            continue
                    else:
                        continue
            except Ingredient.DoesNotExist:
                continue

        # Annotate the queryset with the count of ingredients
        recipe_results = recipe_results.annotate(ingredient_count=Count('recipeingredient'))

        # Paginate the results
        recipe_list = list(
            recipe_results.values('title', 'id', 'ingredient_count')[offset:offset + limit]
        )

        return JsonResponse({
            'recipes': recipe_list,
        })
@method_decorator(login_required, name='dispatch')
class SavePreferences(View):
    def post(self, request):
        data = json.loads(request.body)
        whitelist = data.get('whitelist', [])
        blacklist = data.get('blacklist', [])

        user_preference, created = UserPreference.objects.get_or_create(user=request.user)

        # Update whitelist
        user_preference.whitelist.clear()
        for ingredient_name in whitelist:
            ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_name)
            user_preference.whitelist.add(ingredient)

        # Update blacklist
        user_preference.blacklist.clear()
        for ingredient_name in blacklist:
            ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_name)
            user_preference.blacklist.add(ingredient)

        return JsonResponse({'status': 'success'})

class GetPreferences(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('name', flat=True))
            blacklist = list(user_preference.blacklist.values_list('name', flat=True))
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})

class RecipeDetailView(View):
    def get(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = re.sub(r'\d+\.\s*', '', recipe.instructions.strip())

        # Split instructions by periods
        instructions_list = re.split(r'\.\s+', instructions)

        # add a period to the end of each instruction if it doesn't already have one
        instructions_list = [instruction + '.' if not instruction.endswith('.') else instruction for instruction in instructions_list]

        # Clean up the instructions list
        instructions_list = [instruction.strip() for instruction in instructions_list if instruction]
        
        # Initialize user_rating and user_review to None
        user_rating = None
        user_review = None
        
        if request.user.is_authenticated:
            try:
                # Try to get the user's rating for the recipe
                rating = Rating.objects.get(user=request.user, recipe=recipe)
                user_rating = rating.value
                user_review = rating.review 
            except Rating.DoesNotExist:
                user_rating = None
                user_review = None

        context = {
            'recipe': recipe,
            'is_favorited': is_favorited,
            'instructions_list': instructions_list,
            'user_rating': user_rating,
            'user_review': user_review,
        }
        return render(request, 'cookapp/recipe_detail.html', context)

    def _is_favorited_by_user(self, user, recipe):
        if user.is_authenticated:
            return FavoriteRecipe.objects.filter(user=user, recipe=recipe).exists()
        return False

    @method_decorator(login_required)
    def post(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        try:
            rating_value = int(request.POST.get('rating', 0))
            review_text = request.POST.get('review', '').strip()
            if rating_value < 1 or rating_value > 5:
                return JsonResponse({'status': 'error', 'message': 'Invalid rating value'}, status=400)
            
            # Get or create the rating
            rating, created = Rating.objects.get_or_create(
                user=request.user, 
                recipe=recipe, 
                defaults={'value': rating_value, 'review': review_text}
            )
            # Update the rating value
            rating.value = rating_value
            rating.review = review_text
            rating.save()
            
            # Update the average rating for the recipe
            recipe.update_average_rating()
            
            # Return a success message
            message = 'Rating submitted successfully!' if created else 'Rating updated successfully!'
            return JsonResponse({'status': 'success', 'message': message, 'average_rating': recipe.average_rating})
        except Exception as e:
            print("\n\n!!!! There was an error saving the rating:", e)
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
class ReviewsView(View):
    def get(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html', context)
    
class MealPlanView(View):
    def get(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)

def toggle_favorite(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

@login_required
def favorites(request):
    """
    View to display the user's favorite recipes.
    """
    # Get the favorite recipes for the logged-in user
    favorite_recipes = FavoriteRecipe.objects.filter(user=request.user).select_related('recipe')
    context = {
        'favorite_recipes': favorite_recipes,
    }
    return render(request, 'cookapp/favorites.html', context)

from django.db.models import Avg
from django.views.generic import ListView

class RecipeListView(ListView):
    model = Recipe
    template_name = 'cookapp/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 12

    # Query for recipes depending on filter dropdown
    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=0, then=Value(None)),
                    default='average_rating',
                    output_field=IntegerField(),
                )
            ).order_by('-rating_case', '-average_rating', 'title')  # First by non-zero ratings, then by rating
        elif sort == 'rating_asc':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=0, then=Value(None)),
                    default='average_rating',
                    output_field=IntegerField(),
                )
            ).order_by('rating_case', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset


class RedirectToDetailView(View):
    def post(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})


        
class SimpleRecipeDetailView(View):
    def get(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('term', 'No input')
        whitelist = request.GET.getlist('whitelist', ['No input'])
        blacklist = request.GET.getlist('blacklist', ['No input'])

        # Pass arguments to the context
        context = {
            'search_term': search_term,
            'whitelist': whitelist,
            'blacklist': blacklist,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)

