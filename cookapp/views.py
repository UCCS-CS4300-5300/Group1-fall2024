import json
import re
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe
from django.contrib import messages
import inflect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View
from django.db.models import Q, Count
from django.db.models import Case, When, Value, IntegerField
from .models import (
    Ingredient, Recipe, UserPreference,
    FavoriteRecipe, Diets, Rating, RecipeIngredient
)
from .forms import CreateUserForm, RecipeForm, RecipeIngredientForm
from .decorators import unauthenticated_user
import uuid
from django.forms import modelformset_factory


def index(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = Ingredient.objects.annotate(
        recipe_count=Count('recipeingredient')
    ).order_by('-recipe_count')[:10]

    diets = Diets.objects.annotate(
        diet_count=Count('name')).order_by('-diet_count')

    # Create a dictionary of diet names and blacklisted ingredients
    diet_blacklists = {
        diet.name: list(diet.blacklist.values_list('name', flat=True))
        for diet in diets
    }

    context = {
        'common_ingredients': common_ingredients,
        'diets': diets,
        'diet_blacklists': mark_safe(
            json.dumps(diet_blacklists)),  # Convert for JavaScript access
    }
    return render(request, 'cookapp/index.html', context)


def logout_message(request):
    return render(request, 'registration/logout.html')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        messages.success(
            self.request, f'Welcome back, {form.get_user().username}!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'Invalid username or password. Please try again.')
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

        p = inflect.engine()

        recipe_results = Recipe.objects.all()
        if query:
            recipe_results = recipe_results.filter(
                Q(title__icontains=query) | Q(tags__icontains=query)
            )

        recipe_results = self.apply_whitelist_filter(
            recipe_results, whitelist, p)
        recipe_results = self.apply_blacklist_filter(
            recipe_results, blacklist, p)

        
        recipe_results = recipe_results.annotate(
            ingredient_count=Count('recipeingredient')
        ).order_by('title')

        # Paginate the results
        recipe_list = list(
            recipe_results.values(
                'title', 'id', 'ingredient_count'
            )[offset:offset + limit]
        )

        return JsonResponse({'recipes': recipe_list})

    def apply_whitelist_filter(self, queryset, whitelist, inflect_engine):
        for ingredient in whitelist:
            queryset = self.filter_by_ingredient(
                queryset, ingredient, inflect_engine, include=True)
            if queryset is None:
                return Recipe.objects.none()
        return queryset

    def apply_blacklist_filter(self, queryset, blacklist, inflect_engine):
        for ingredient in blacklist:
            queryset = self.filter_by_ingredient(
                queryset, ingredient, inflect_engine, include=False)
        return queryset

    def filter_by_ingredient(self, queryset,
                             ingredient, inflect_engine, include=True):
        try:
            ingredients = Ingredient.objects.filter(
                name__icontains=ingredient).distinct()
            if not ingredients.exists():
                singular_ingredient = inflect_engine.singular_noun(ingredient)
                if singular_ingredient:
                    ingredients = Ingredient.objects.filter(
                        name__icontains=singular_ingredient).distinct()
            if ingredients.exists():
                if include:
                    return queryset.filter(
                        recipeingredient__ingredient__in=ingredients)
                else:
                    return queryset.exclude(
                        recipeingredient__ingredient__in=ingredients)
            elif include:
                return None
        except Ingredient.DoesNotExist:
            if include:
                return None
        return queryset



@method_decorator(login_required, name='dispatch')
class SavePreferences(View):
    def post(self, request):
        data = json.loads(request.body)
        whitelist = data.get('whitelist', [])
        blacklist = data.get('blacklist', [])

        user_preference, created = UserPreference.objects.get_or_create(
            user=request.user)

        # Update whitelist
        user_preference.whitelist.clear()
        for ingredient_name in whitelist:
            ingredient, _ = Ingredient.objects.get_or_create(
                name=ingredient_name)
            user_preference.whitelist.add(ingredient)

        # Update blacklist
        user_preference.blacklist.clear()
        for ingredient_name in blacklist:
            ingredient, _ = Ingredient.objects.get_or_create(
                name=ingredient_name)
            user_preference.blacklist.add(ingredient)

        return JsonResponse({'status': 'success'})


class GetPreferences(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(
                user=request.user
            )
            whitelist = list(
                user_preference.whitelist.values_list('name', flat=True)
            )
            blacklist = list(
                user_preference.blacklist.values_list('name', flat=True)
            )
            return JsonResponse({
                'whitelist': whitelist,
                'blacklist': blacklist
            })
        return JsonResponse({'whitelist': [], 'blacklist': []})


class RecipeDetailView(View):
    def get(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorite_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = re.sub(r'\d+\.\s*', '', recipe.instructions.strip())

        # Split instructions by periods
        instructions_list = re.split(r'\.\s+', instructions)

        # Add a period to the end of each instruction
        instructions_list = [
            instruction + '.' if not instruction.endswith('.')
            else instruction
            for instruction in instructions_list
        ]

        # Clean up the instructions list
        instructions_list = [
            instruction.strip()
            for instruction in instructions_list
            if instruction
        ]
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

    def _is_favorite_by_user(self, user, recipe):
        if user.is_authenticated:
            return FavoriteRecipe.objects.filter(
                user=user, recipe=recipe
            ).exists()
        return False

    @method_decorator(login_required)
    def post(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        try:
            rating_value = int(request.POST.get('rating', 0))
            review_text = request.POST.get('review', '').strip()
            if rating_value < 1 or rating_value > 5:
                return JsonResponse(
                    {'status': 'error', 'message': 'Invalid rating value'},
                    status=400)

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
            message = (
                'Rating submitted successfully!'
                if created
                else 'Rating updated successfully!'
            )
            return JsonResponse(
                {'status': 'success',
                 'message': message,
                 'average_rating': recipe.average_rating})
        except Exception as e:
            print("\n\n!!!! There was an error saving the rating:", e)
            return JsonResponse(
                {'status': 'error', 'message': str(e)},
                status=500)


class ReviewsView(View):
    def get(self, request):
        reviews = Rating.objects.filter(
            review__isnull=False
        ).select_related('recipe', 'user')
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html', context)


class UserReviewsView(LoginRequiredMixin, View):
    def get(self, request):
        reviews = Rating.objects.filter(user=request.user)\
            .select_related('recipe')
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html', context)


@require_POST
def delete_review(request, rating_id):
    try:
        rating = get_object_or_404(Rating, id=rating_id)
        # Get the recipe ID before deleting the rating
        recipe_id = rating.recipe.id
        rating.delete()
        messages.success(request, 'Review deleted successfully')
        return redirect('recipe_detail', id=recipe_id)
    except Exception as e:
        messages.error(request, f'Error deleting review: {e}')
        return redirect('recipe_detail', id=recipe_id)


class MealPlanView(View):
    def get(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
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
        favorite, created = FavoriteRecipe.objects.get_or_create(
            user=request.user, recipe=recipe)
        # If it was not created, it means it already exists, so remove it
        if not created:
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)


@login_required
def favorites(request):
    """
    View to display the user's favorite recipes.
    """
    # Get the favorite recipes for the logged-in user
    favorite_recipes = FavoriteRecipe.objects.filter(
        user=request.user).select_related('recipe')
    context = {
        'favorite_recipes': favorite_recipes,
    }
    return render(request, 'cookapp/favorites.html', context)


class RecipeListView(ListView):
    model = Recipe
    template_name = 'cookapp/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 12

    # Query for recipes depending on filter dropdown
    def get_queryset(self):
        queryset = super().get_queryset()
        # Default to 'name' for A-Z sorting
        sort = self.request.GET.get('sort', 'name')

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=0, then=Value(None)),
                    default='average_rating',
                    output_field=IntegerField(),
                )
                # First by non-zero ratings, then by rating
            ).order_by('-rating_case', '-average_rating', 'title')
        elif sort == 'rating_asc':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=0, then=Value(None)),
                    default='average_rating',
                    output_field=IntegerField(),
                )
                # First by non-zero ratings, then by rating
            ).order_by('rating_case', 'average_rating', 'title')
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
        redirect_url = f'''/simple-recipe-detail/?term={search_term}
                            &whitelist={"&whitelist=".join(whitelist)}
                            &blacklist={"&blacklist=".join(blacklist)}'''
        return JsonResponse({'redirect_url': redirect_url})


class SimpleRecipeDetailView(View):
    def get(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('term', 'No input')
        whitelist = request.GET.getlist('whitelist', ['No input'])
        blacklist = request.GET.getlist('blacklist', ['No input'])

        # Fetch recipes based on search term, whitelist, and blacklist
        recipes = Recipe.objects.all()
        if search_term:
            recipes = recipes.filter(
                Q(title__icontains=search_term) |
                Q(tags__icontains=search_term)
            )

        for ingredient in whitelist:
            recipes = recipes.filter(
                recipe_ingredient__ingredient__name__icontains=ingredient
            )
        for ingredient in blacklist:
            recipes = recipes.exclude(
                recipe_ingredient__ingredient__name__icontains=ingredient
            )

        # Pass arguments and recipes to the context
        context = {
            'search_term': search_term,
            'whitelist': whitelist,
            'blacklist': blacklist,
            'recipes': recipes,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            # If the recipe doesn't have an API ID, generate one
            if not recipe.api_id:
                recipe.api_id = str(uuid.uuid4())

            recipe.save()

            return redirect('add_ingredients', recipe_id=recipe.id)
    else:
        form = RecipeForm()

    return render(request, 'cookapp/create_recipe.html', {'form': form})


# Define the formset for RecipeIngredient in the views
RecipeIngredientFormSet = modelformset_factory(
    RecipeIngredient,
    form=RecipeIngredientForm,
    extra=1,  # Allows up to 5 ingredients to be added
)


def add_ingredients(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(
            request.POST,
            queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            for form in formset:  # Save the valid forms with data
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            return redirect('index')  # Redirect after saving
    else:
        formset = RecipeIngredientFormSet(
            queryset=RecipeIngredient.objects.none()
        )

    return render(request,
                  'cookapp/add_ingredients.html',
                  {'formset': formset, 'recipe': recipe})
