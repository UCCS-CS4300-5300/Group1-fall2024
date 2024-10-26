# cookapp/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    
    # Search functionality
    path('search/', views.RecipeSearch.as_view(), name='recipe_search'),
    
    # Recipe detail page
    path('recipe/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),

    # User preferences
    path('save_preferences/', views.SavePreferences.as_view(), name='save_preferences'),
    path('get_preferences/', views.GetPreferences.as_view(), name='get_preferences'),
    
    # User authentication
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name='register_page'),
    path('logout/', views.logout_message, name='logout_message'),
    
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
