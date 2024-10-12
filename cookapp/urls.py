from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.RecipeSearch.as_view(), name='recipe_search'),
]