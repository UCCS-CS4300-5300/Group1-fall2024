
from django.urls import path, include
from . import views
from .views import (
    SimpleRecipeDetailView,
    RedirectToDetailView,
)

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Search functionality
    path('search/', views.RecipeSearch.as_view(), name='recipe_search'),

    # List of all Recipes
    path('recipes/', views.RecipeListView.as_view(), name='recipes'),
    # Recipe detail page
    path('recipe/<int:id>/',
         views.RecipeDetailView.as_view(), name='recipe_detail'),

    # User preferences
    path('save_preferences/',
         views.SavePreferences.as_view(), name='save_preferences'),
    path('get_preferences/',
         views.GetPreferences.as_view(), name='get_preferences'),
    # Meal plan
    path('mealplan/', views.MealPlanView.as_view(), name='meal_plan'),
    # User authentication
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name='register_page'),
    path('logout/', views.logout_message, name='logout_message'),
    # User reviews
    path('reviews/', views.UserReviewsView.as_view(), name='reviews'),
    path('delete_review/<int:rating_id>/',
         views.delete_review, name='delete_review'),

    # Simplified AI recipe generator
    path('simple-recipe-detail/',
         SimpleRecipeDetailView.as_view(), name='simple_recipe_detail'),
    path('redirect-to-detail/',
         RedirectToDetailView.as_view(), name='redirect_to_detail'),
    path('generate-recipe/',
         RedirectToDetailView.as_view(), name='generate_recipe'),

    # Favorite functionality
    path('recipe/<int:recipe_id>/toggle_favorite/',
         views.toggle_favorite, name='toggle_favorite'),
    path('profile/favorites/',
         views.favorites, name='favorites'),

    path('create/', views.create_recipe, name='create_recipe'),
    path('add-ingredients/<int:recipe_id>/',
         views.add_ingredients, name='add_ingredients'),
]
