import json
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe
from django.contrib import messages

from django.http import JsonResponse
from django.views import View
from django.db.models import Q, Count

from .models import Ingredient, Recipe, UserPreference, FavoriteRecipe, Diets
from .forms import CreateUserForm
from .decorators import unauthenticated_user

def index(request):
    # Get the most common ingredients
    # works by counting the number of recipes that use each ingredient and ordering by that count
    # annotate adds a new field to each ingredient object with the count
    common_ingredients = Ingredient.objects.annotate(recipe_count=Count('recipe')).order_by('-recipe_count')[:10]
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
            print(f'Messages: {messages.get_messages(request)}')  # Debugging line
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

        # Initialize the query
        if query:
            recipe_results = Recipe.objects.filter(Q(title__icontains=query) | Q(tags__icontains=query))
        else:
            recipe_results = Recipe.objects.all()

        # Apply whitelist filter (include only recipes with all specified whitelist ingredients)
        if whitelist:
            for ingredient in whitelist:
                try:
                    whitelisted_ingredient = Ingredient.objects.get(name__iexact=ingredient)
                    recipe_results = recipe_results.filter(recipeingredient__ingredient=whitelisted_ingredient)
                except Ingredient.DoesNotExist:
                    # If any ingredient in the whitelist is not found, no recipes can match
                    return JsonResponse({'recipes': []})

        # Apply blacklist filter
        for ingredient in blacklist:
            try:
                blacklisted_ingredient = Ingredient.objects.get(name__iexact=ingredient)
                recipe_results = recipe_results.exclude(recipeingredient__ingredient=blacklisted_ingredient)
            except Ingredient.DoesNotExist:
                continue

        # Paginate the results
        recipe_list = list(recipe_results.distinct().values('title', 'id')[offset:offset + limit])

        # Add ingredient count to each recipe
        for recipe in recipe_list:
            recipe_obj = Recipe.objects.get(id=recipe['id'])
            recipe['ingredient_count'] = recipe_obj.ingredients.count()

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
            user_preference, created = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('name', flat=True))
            blacklist = list(user_preference.blacklist.values_list('name', flat=True))
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})

class RecipeDetailView(View):
    def get(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        
        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Check if the instructions contain numbered steps
        if re.search(r'\d+\.\s*', recipe.instructions):
            # Split instructions using a regular expression to capture numbered steps
            instructions_list = re.split(r'(?<=\d\.)\s*', recipe.instructions.strip())
        else:
            # Split by period and space
            instructions_list = re.split(r'\.\s+', recipe.instructions.strip())
            # Add a new period to the end of each instruction
            instructions_list = [instruction + '.' for instruction in instructions_list if instruction]

        # Clean up the instructions list
        instructions_list = [instruction.strip() for instruction in instructions_list if instruction]

        context = {
            'recipe': recipe,
            'is_favorited': is_favorited,
            'instructions_list': instructions_list,
        }
        return render(request, 'cookapp/recipe_detail.html', context)
    
    def _is_favorited_by_user(self, user, recipe):
        if user.is_authenticated:
            return FavoriteRecipe.objects.filter(user=user, recipe=recipe).exists()
        return False
    
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