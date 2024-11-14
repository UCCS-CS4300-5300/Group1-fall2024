
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


# cookapp/urls.py

from django.urls import path, include
from . import views

from django.urls import path, include
from . import views
from .views import SimpleRecipeDetailView, RedirectToDetailView  # Import the new views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    
    # Search functionality
    path('search/', views.RecipeSearch.as_view(), name='recipe_search'),

    # List of all Recipes
    path('recipes/', views.RecipeListView.as_view(), name='recipes'),
    
    # Recipe detail page
    path('recipe/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),

    # User preferences
    path('save_preferences/', views.SavePreferences.as_view(), name='save_preferences'),
    path('get_preferences/', views.GetPreferences.as_view(), name='get_preferences'),
    
    # Meal plan
    path('mealplan/', views.MealPlanView.as_view(), name='meal_plan'),
    
    # User authentication
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name='register_page'),
    path('logout/', views.logout_message, name='logout_message'),
    
 
    # User reviews
    path('reviews/', views.ReviewsView.as_view(), name='reviews'),


    # Simplified AI recipe generator
    path('simple-recipe-detail/', SimpleRecipeDetailView.as_view(), name='simple_recipe_detail'),
    path('redirect-to-detail/', RedirectToDetailView.as_view(), name='redirect_to_detail'),
    path('generate-recipe/', RedirectToDetailView.as_view(), name='generate_recipe'),
    # Favorite functionality
    path('recipe/<int:recipe_id>/toggle_favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('profile/favorites/', views.favorites, name='favorites'),

    path('create/', views.create_recipe, name='create_recipe'),
    path('add-ingredients/<int:recipe_id>/', views.add_ingredients, name='add_ingredients'),
    
    # Django's built-in authentication URL patterns (for reference)
    # accounts/login/          [name='login']
    # accounts/logout/         [name='logout']
    # accounts/password_change/         [name='password_change']
    # accounts/password_change/done/    [name='password_change_done']
    # accounts/password_reset/          [name='password_reset']
    # accounts/password_reset/done/     [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/  [name='password_reset_confirm']
    # accounts/reset/done/              [name='password_reset_complete']
]
