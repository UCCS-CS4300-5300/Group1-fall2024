from django.shortcuts import render, redirect
from .models import Ingredient, Recipe, UserPreference
from .decorators import unauthenticated_user
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import json
from django.http import JsonResponse
from django.views import View
from django.db.models import Q


def index(request):
    return render(request, 'cookapp/index.html')

def logout_message(request):
    return render(request, 'registration/logout.html')

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            user.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'registration/register.html', context)

class RecipeSearch(View):
    def get(self, request):
        query = request.GET.get('term', '')
        blacklist_query = request.GET.get('blacklist', '[]')

        # Parse the blacklist JSON string into a list
        try:
            blacklist = json.loads(blacklist_query)
        except json.JSONDecodeError:
            blacklist = []

        # Search by Recipe title or tags
        recipe_results = Recipe.objects.filter(Q(title__icontains=query) | Q(tags__icontains=query))

        # Exclude recipes with blacklisted ingredients
        for ingredient in blacklist:
            try:
                blacklisted_ingredient = Ingredient.objects.get(name__iexact=ingredient)
                recipe_results = recipe_results.exclude(ingredients=blacklisted_ingredient)
            except Ingredient.DoesNotExist:
                pass  # If the ingredient doesn't exist, just skip filtering for it

        # Limit results to 10 and prepare response data
        recipe_list = list(recipe_results.values('title', 'id')[:10])

        return JsonResponse({
            'recipes': recipe_list,
        }, safe=False)