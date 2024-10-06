from django.shortcuts import render
from .models import Ingredient, Recipe, UserPreference

def index(request):
    return render(request, 'index.html')
