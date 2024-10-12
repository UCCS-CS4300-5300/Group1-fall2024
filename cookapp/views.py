from django.shortcuts import render
from .models import Ingredient, Recipe, UserPreference
from django.http import JsonResponse
from django.views import View

def index(request):
    return render(request, 'index.html')

class RecipeSearch(View):
    def get(self, request):
        query = request.GET.get('term', '')
        
        # Search by Recipe title or tags
        recipe_results = Recipe.objects.filter(title__icontains=query)[:10]  # Limit results to 10
        tag_results = Recipe.objects.filter(tags__icontains=query)[:10]  # Limit results to 10

        # Prepare response data
        recipe_list = list(recipe_results.values('title'))
        tag_list = list(tag_results.values('title'))

        # Combine and remove duplicates
        combined_list = {item['title']: item for item in recipe_list + tag_list}.values()

        return JsonResponse({
            'recipes': list(combined_list),
        }, safe=False)