
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


def x_index__mutmut_orig(request):
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


def x_index__mutmut_1(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = Ingredient.objects.annotate(
        recipe_count=Count('XXrecipeingredientXX')
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


def x_index__mutmut_2(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = Ingredient.objects.annotate(
        recipe_count=Count('recipeingredient')
    ).order_by('XX-recipe_countXX')[:10]

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


def x_index__mutmut_3(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = Ingredient.objects.annotate(
        recipe_count=Count('recipeingredient')
    ).order_by('-recipe_count')[:11]

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


def x_index__mutmut_4(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = Ingredient.objects.annotate(
        recipe_count=Count('recipeingredient')
    ).order_by('-recipe_count')[None]

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


def x_index__mutmut_5(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = None

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


def x_index__mutmut_6(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = Ingredient.objects.annotate(
        recipe_count=Count('recipeingredient')
    ).order_by('-recipe_count')[:10]

    diets = Diets.objects.annotate(diet_count=Count('XXnameXX')).order_by('-diet_count')

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


def x_index__mutmut_7(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = Ingredient.objects.annotate(
        recipe_count=Count('recipeingredient')
    ).order_by('-recipe_count')[:10]

    diets = Diets.objects.annotate(diet_count=Count('name')).order_by('XX-diet_countXX')

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


def x_index__mutmut_8(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = Ingredient.objects.annotate(
        recipe_count=Count('recipeingredient')
    ).order_by('-recipe_count')[:10]

    diets = None

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


def x_index__mutmut_9(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = Ingredient.objects.annotate(
        recipe_count=Count('recipeingredient')
    ).order_by('-recipe_count')[:10]

    diets = Diets.objects.annotate(diet_count=Count('name')).order_by('-diet_count')

    # Create a dictionary of diet names and their respective blacklisted ingredients
    diet_blacklists = {
        diet.name: list(diet.blacklist.values_list('XXnameXX', flat=True))
        for diet in diets
    }

    context = {
        'common_ingredients': common_ingredients,
        'diets': diets,
        'diet_blacklists': mark_safe(json.dumps(diet_blacklists)),  # Convert to JSON for JavaScript access
    }
    return render(request, 'cookapp/index.html', context)


def x_index__mutmut_10(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = Ingredient.objects.annotate(
        recipe_count=Count('recipeingredient')
    ).order_by('-recipe_count')[:10]

    diets = Diets.objects.annotate(diet_count=Count('name')).order_by('-diet_count')

    # Create a dictionary of diet names and their respective blacklisted ingredients
    diet_blacklists = {
        diet.name: list(diet.blacklist.values_list('name', flat=False))
        for diet in diets
    }

    context = {
        'common_ingredients': common_ingredients,
        'diets': diets,
        'diet_blacklists': mark_safe(json.dumps(diet_blacklists)),  # Convert to JSON for JavaScript access
    }
    return render(request, 'cookapp/index.html', context)


def x_index__mutmut_11(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = Ingredient.objects.annotate(
        recipe_count=Count('recipeingredient')
    ).order_by('-recipe_count')[:10]

    diets = Diets.objects.annotate(diet_count=Count('name')).order_by('-diet_count')

    # Create a dictionary of diet names and their respective blacklisted ingredients
    diet_blacklists = {
        diet.name: list(diet.blacklist.values_list('name',))
        for diet in diets
    }

    context = {
        'common_ingredients': common_ingredients,
        'diets': diets,
        'diet_blacklists': mark_safe(json.dumps(diet_blacklists)),  # Convert to JSON for JavaScript access
    }
    return render(request, 'cookapp/index.html', context)


def x_index__mutmut_12(request):
    # Count recipes by referencing the related `recipeingredient` set
    common_ingredients = Ingredient.objects.annotate(
        recipe_count=Count('recipeingredient')
    ).order_by('-recipe_count')[:10]

    diets = Diets.objects.annotate(diet_count=Count('name')).order_by('-diet_count')

    # Create a dictionary of diet names and their respective blacklisted ingredients
    diet_blacklists = None

    context = {
        'common_ingredients': common_ingredients,
        'diets': diets,
        'diet_blacklists': mark_safe(json.dumps(diet_blacklists)),  # Convert to JSON for JavaScript access
    }
    return render(request, 'cookapp/index.html', context)


def x_index__mutmut_13(request):
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
        'XXcommon_ingredientsXX': common_ingredients,
        'diets': diets,
        'diet_blacklists': mark_safe(json.dumps(diet_blacklists)),  # Convert to JSON for JavaScript access
    }
    return render(request, 'cookapp/index.html', context)


def x_index__mutmut_14(request):
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
        'XXdietsXX': diets,
        'diet_blacklists': mark_safe(json.dumps(diet_blacklists)),  # Convert to JSON for JavaScript access
    }
    return render(request, 'cookapp/index.html', context)


def x_index__mutmut_15(request):
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
        'XXdiet_blacklistsXX': mark_safe(json.dumps(diet_blacklists)),  # Convert to JSON for JavaScript access
    }
    return render(request, 'cookapp/index.html', context)


def x_index__mutmut_16(request):
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
        'diet_blacklists': mark_safe(json.dumps(None)),  # Convert to JSON for JavaScript access
    }
    return render(request, 'cookapp/index.html', context)


def x_index__mutmut_17(request):
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

    context = None
    return render(request, 'cookapp/index.html', context)


def x_index__mutmut_18(request):
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
    return render(None, 'cookapp/index.html', context)


def x_index__mutmut_19(request):
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
    return render(request, 'XXcookapp/index.htmlXX', context)


def x_index__mutmut_20(request):
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
    return render(request, 'cookapp/index.html', None)


def x_index__mutmut_21(request):
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
    return render( 'cookapp/index.html', context)


def x_index__mutmut_22(request):
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
    return render(request, 'cookapp/index.html',)

x_index__mutmut_mutants = {
'x_index__mutmut_1': x_index__mutmut_1, 
    'x_index__mutmut_2': x_index__mutmut_2, 
    'x_index__mutmut_3': x_index__mutmut_3, 
    'x_index__mutmut_4': x_index__mutmut_4, 
    'x_index__mutmut_5': x_index__mutmut_5, 
    'x_index__mutmut_6': x_index__mutmut_6, 
    'x_index__mutmut_7': x_index__mutmut_7, 
    'x_index__mutmut_8': x_index__mutmut_8, 
    'x_index__mutmut_9': x_index__mutmut_9, 
    'x_index__mutmut_10': x_index__mutmut_10, 
    'x_index__mutmut_11': x_index__mutmut_11, 
    'x_index__mutmut_12': x_index__mutmut_12, 
    'x_index__mutmut_13': x_index__mutmut_13, 
    'x_index__mutmut_14': x_index__mutmut_14, 
    'x_index__mutmut_15': x_index__mutmut_15, 
    'x_index__mutmut_16': x_index__mutmut_16, 
    'x_index__mutmut_17': x_index__mutmut_17, 
    'x_index__mutmut_18': x_index__mutmut_18, 
    'x_index__mutmut_19': x_index__mutmut_19, 
    'x_index__mutmut_20': x_index__mutmut_20, 
    'x_index__mutmut_21': x_index__mutmut_21, 
    'x_index__mutmut_22': x_index__mutmut_22
}

def index(*args, **kwargs):
    result = _mutmut_trampoline(x_index__mutmut_orig, x_index__mutmut_mutants, *args, **kwargs)
    return result 

index.__signature__ = _mutmut_signature(x_index__mutmut_orig)
x_index__mutmut_orig.__name__ = 'x_index'



def x_logout_message__mutmut_orig(request):
    return render(request, 'registration/logout.html')

def x_logout_message__mutmut_1(request):
    return render(None, 'registration/logout.html')

def x_logout_message__mutmut_2(request):
    return render(request, 'XXregistration/logout.htmlXX')

def x_logout_message__mutmut_3(request):
    return render( 'registration/logout.html')

x_logout_message__mutmut_mutants = {
'x_logout_message__mutmut_1': x_logout_message__mutmut_1, 
    'x_logout_message__mutmut_2': x_logout_message__mutmut_2, 
    'x_logout_message__mutmut_3': x_logout_message__mutmut_3
}

def logout_message(*args, **kwargs):
    result = _mutmut_trampoline(x_logout_message__mutmut_orig, x_logout_message__mutmut_mutants, *args, **kwargs)
    return result 

logout_message.__signature__ = _mutmut_signature(x_logout_message__mutmut_orig)
x_logout_message__mutmut_orig.__name__ = 'x_logout_message'



class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def xǁCustomLoginViewǁform_valid__mutmut_orig(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().username}!')
        return super().form_valid(form)

    def xǁCustomLoginViewǁform_valid__mutmut_1(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().username}!')
        return super().form_valid(None)

    xǁCustomLoginViewǁform_valid__mutmut_mutants = {
    'xǁCustomLoginViewǁform_valid__mutmut_1': xǁCustomLoginViewǁform_valid__mutmut_1
    }

    def form_valid(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCustomLoginViewǁform_valid__mutmut_orig"), object.__getattribute__(self, "xǁCustomLoginViewǁform_valid__mutmut_mutants"), *args, **kwargs)
        return result 

    form_valid.__signature__ = _mutmut_signature(xǁCustomLoginViewǁform_valid__mutmut_orig)
    xǁCustomLoginViewǁform_valid__mutmut_orig.__name__ = 'xǁCustomLoginViewǁform_valid'



    def xǁCustomLoginViewǁform_invalid__mutmut_orig(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)

    def xǁCustomLoginViewǁform_invalid__mutmut_1(self, form):
        messages.error(self.request, 'XXInvalid username or password. Please try again.XX')
        return super().form_invalid(form)

    def xǁCustomLoginViewǁform_invalid__mutmut_2(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(None)

    xǁCustomLoginViewǁform_invalid__mutmut_mutants = {
    'xǁCustomLoginViewǁform_invalid__mutmut_1': xǁCustomLoginViewǁform_invalid__mutmut_1, 
        'xǁCustomLoginViewǁform_invalid__mutmut_2': xǁCustomLoginViewǁform_invalid__mutmut_2
    }

    def form_invalid(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCustomLoginViewǁform_invalid__mutmut_orig"), object.__getattribute__(self, "xǁCustomLoginViewǁform_invalid__mutmut_mutants"), *args, **kwargs)
        return result 

    form_invalid.__signature__ = _mutmut_signature(xǁCustomLoginViewǁform_invalid__mutmut_orig)
    xǁCustomLoginViewǁform_invalid__mutmut_orig.__name__ = 'xǁCustomLoginViewǁform_invalid'



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
    def xǁRecipeSearchǁget__mutmut_orig(self, request):
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
    def xǁRecipeSearchǁget__mutmut_1(self, request):
        query = request.GET.get('XXtermXX', '').strip()
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
    def xǁRecipeSearchǁget__mutmut_2(self, request):
        query = request.GET.get('term', 'XXXX').strip()
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
    def xǁRecipeSearchǁget__mutmut_3(self, request):
        query = None
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
    def xǁRecipeSearchǁget__mutmut_4(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('XXblacklistXX', '[]')
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
    def xǁRecipeSearchǁget__mutmut_5(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', 'XX[]XX')
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
    def xǁRecipeSearchǁget__mutmut_6(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = None
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
    def xǁRecipeSearchǁget__mutmut_7(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('XXwhitelistXX', '[]')
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
    def xǁRecipeSearchǁget__mutmut_8(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('whitelist', 'XX[]XX')
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
    def xǁRecipeSearchǁget__mutmut_9(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = None
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
    def xǁRecipeSearchǁget__mutmut_10(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('whitelist', '[]')
        offset = int(request.GET.get('XXoffsetXX', 0))
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
    def xǁRecipeSearchǁget__mutmut_11(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('whitelist', '[]')
        offset = int(request.GET.get('offset', 1))
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
    def xǁRecipeSearchǁget__mutmut_12(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('whitelist', '[]')
        offset = None
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
    def xǁRecipeSearchǁget__mutmut_13(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('whitelist', '[]')
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('XXlimitXX', 10))

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
    def xǁRecipeSearchǁget__mutmut_14(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('whitelist', '[]')
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 11))

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
    def xǁRecipeSearchǁget__mutmut_15(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('whitelist', '[]')
        offset = int(request.GET.get('offset', 0))
        limit = None

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
    def xǁRecipeSearchǁget__mutmut_16(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('whitelist', '[]')
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 10))

        try:
            blacklist = json.loads(None)
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
    def xǁRecipeSearchǁget__mutmut_17(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('whitelist', '[]')
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 10))

        try:
            blacklist = None
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
    def xǁRecipeSearchǁget__mutmut_18(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('whitelist', '[]')
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 10))

        try:
            blacklist = json.loads(blacklist_query)
            whitelist = json.loads(None)
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
    def xǁRecipeSearchǁget__mutmut_19(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('whitelist', '[]')
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 10))

        try:
            blacklist = json.loads(blacklist_query)
            whitelist = None
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
    def xǁRecipeSearchǁget__mutmut_20(self, request):
        query = request.GET.get('term', '').strip()
        blacklist_query = request.GET.get('blacklist', '[]')
        whitelist_query = request.GET.get('whitelist', '[]')
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 10))

        try:
            blacklist = json.loads(blacklist_query)
            whitelist = json.loads(whitelist_query)
        except json.JSONDecodeError:
            blacklist = None
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
    def xǁRecipeSearchǁget__mutmut_21(self, request):
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
            whitelist = None

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
    def xǁRecipeSearchǁget__mutmut_22(self, request):
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
        p = None

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
    def xǁRecipeSearchǁget__mutmut_23(self, request):
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
                Q(title__icontains=None) | Q(tags__icontains=query)
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
    def xǁRecipeSearchǁget__mutmut_24(self, request):
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
                Q(title__icontains=query) & Q(tags__icontains=query)
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
    def xǁRecipeSearchǁget__mutmut_25(self, request):
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
                Q(title__icontains=query) | Q(tags__icontains=None)
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
    def xǁRecipeSearchǁget__mutmut_26(self, request):
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
            recipe_results = None
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
    def xǁRecipeSearchǁget__mutmut_27(self, request):
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
            recipe_results = None

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
    def xǁRecipeSearchǁget__mutmut_28(self, request):
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
                    whitelisted_ingredients = Ingredient.objects.filter(name__icontains=None).distinct()
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
    def xǁRecipeSearchǁget__mutmut_29(self, request):
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
                    whitelisted_ingredients = None
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
    def xǁRecipeSearchǁget__mutmut_30(self, request):
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
                        recipe_results = recipe_results.filter(recipeingredient__ingredient__in=None)
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
    def xǁRecipeSearchǁget__mutmut_31(self, request):
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
                        recipe_results = None
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
    def xǁRecipeSearchǁget__mutmut_32(self, request):
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
                        singular_ingredient = p.singular_noun(None)
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
    def xǁRecipeSearchǁget__mutmut_33(self, request):
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
                        singular_ingredient = None
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
    def xǁRecipeSearchǁget__mutmut_34(self, request):
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
                            whitelisted_ingredients = Ingredient.objects.filter(name__icontains=None).distinct()
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
    def xǁRecipeSearchǁget__mutmut_35(self, request):
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
                            whitelisted_ingredients = None
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
    def xǁRecipeSearchǁget__mutmut_36(self, request):
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
                                recipe_results = recipe_results.filter(recipeingredient__ingredient__in=None)
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
    def xǁRecipeSearchǁget__mutmut_37(self, request):
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
                                recipe_results = None
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
    def xǁRecipeSearchǁget__mutmut_38(self, request):
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
                                    'XXrecipesXX': [],
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
    def xǁRecipeSearchǁget__mutmut_39(self, request):
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
                                'XXrecipesXX': [],
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
    def xǁRecipeSearchǁget__mutmut_40(self, request):
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
                    return JsonResponse({'XXrecipesXX': []})

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
    def xǁRecipeSearchǁget__mutmut_41(self, request):
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
                blacklisted_ingredients = Ingredient.objects.filter(name__icontains=None).distinct()
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
    def xǁRecipeSearchǁget__mutmut_42(self, request):
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
                blacklisted_ingredients = None
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
    def xǁRecipeSearchǁget__mutmut_43(self, request):
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
                    recipe_results = recipe_results.exclude(recipeingredient__ingredient__in=None)
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
    def xǁRecipeSearchǁget__mutmut_44(self, request):
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
                    recipe_results = None
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
    def xǁRecipeSearchǁget__mutmut_45(self, request):
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
                    singular_ingredient = p.singular_noun(None)
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
    def xǁRecipeSearchǁget__mutmut_46(self, request):
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
                    singular_ingredient = None
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
    def xǁRecipeSearchǁget__mutmut_47(self, request):
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
                        blacklisted_ingredients = Ingredient.objects.filter(name__icontains=None).distinct()
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
    def xǁRecipeSearchǁget__mutmut_48(self, request):
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
                        blacklisted_ingredients = None
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
    def xǁRecipeSearchǁget__mutmut_49(self, request):
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
                            recipe_results = recipe_results.exclude(recipeingredient__ingredient__in=None)
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
    def xǁRecipeSearchǁget__mutmut_50(self, request):
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
                            recipe_results = None
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
    def xǁRecipeSearchǁget__mutmut_51(self, request):
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
                            break
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
    def xǁRecipeSearchǁget__mutmut_52(self, request):
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
                        break
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
    def xǁRecipeSearchǁget__mutmut_53(self, request):
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
                break

        # Annotate the queryset with the count of ingredients
        recipe_results = recipe_results.annotate(ingredient_count=Count('recipeingredient'))

        # Paginate the results
        recipe_list = list(
            recipe_results.values('title', 'id', 'ingredient_count')[offset:offset + limit]
        )

        return JsonResponse({
            'recipes': recipe_list,
        })
    def xǁRecipeSearchǁget__mutmut_54(self, request):
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
        recipe_results = recipe_results.annotate(ingredient_count=Count('XXrecipeingredientXX'))

        # Paginate the results
        recipe_list = list(
            recipe_results.values('title', 'id', 'ingredient_count')[offset:offset + limit]
        )

        return JsonResponse({
            'recipes': recipe_list,
        })
    def xǁRecipeSearchǁget__mutmut_55(self, request):
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
        recipe_results = None

        # Paginate the results
        recipe_list = list(
            recipe_results.values('title', 'id', 'ingredient_count')[offset:offset + limit]
        )

        return JsonResponse({
            'recipes': recipe_list,
        })
    def xǁRecipeSearchǁget__mutmut_56(self, request):
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
            recipe_results.values('XXtitleXX', 'id', 'ingredient_count')[offset:offset + limit]
        )

        return JsonResponse({
            'recipes': recipe_list,
        })
    def xǁRecipeSearchǁget__mutmut_57(self, request):
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
            recipe_results.values('title', 'XXidXX', 'ingredient_count')[offset:offset + limit]
        )

        return JsonResponse({
            'recipes': recipe_list,
        })
    def xǁRecipeSearchǁget__mutmut_58(self, request):
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
            recipe_results.values('title', 'id', 'XXingredient_countXX')[offset:offset + limit]
        )

        return JsonResponse({
            'recipes': recipe_list,
        })
    def xǁRecipeSearchǁget__mutmut_59(self, request):
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
            recipe_results.values('title', 'id', 'ingredient_count')[offset:offset - limit]
        )

        return JsonResponse({
            'recipes': recipe_list,
        })
    def xǁRecipeSearchǁget__mutmut_60(self, request):
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
            recipe_results.values('title', 'id', 'ingredient_count')[None]
        )

        return JsonResponse({
            'recipes': recipe_list,
        })
    def xǁRecipeSearchǁget__mutmut_61(self, request):
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
        recipe_list = None

        return JsonResponse({
            'recipes': recipe_list,
        })
    def xǁRecipeSearchǁget__mutmut_62(self, request):
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
            'XXrecipesXX': recipe_list,
        })

    xǁRecipeSearchǁget__mutmut_mutants = {
    'xǁRecipeSearchǁget__mutmut_1': xǁRecipeSearchǁget__mutmut_1, 
        'xǁRecipeSearchǁget__mutmut_2': xǁRecipeSearchǁget__mutmut_2, 
        'xǁRecipeSearchǁget__mutmut_3': xǁRecipeSearchǁget__mutmut_3, 
        'xǁRecipeSearchǁget__mutmut_4': xǁRecipeSearchǁget__mutmut_4, 
        'xǁRecipeSearchǁget__mutmut_5': xǁRecipeSearchǁget__mutmut_5, 
        'xǁRecipeSearchǁget__mutmut_6': xǁRecipeSearchǁget__mutmut_6, 
        'xǁRecipeSearchǁget__mutmut_7': xǁRecipeSearchǁget__mutmut_7, 
        'xǁRecipeSearchǁget__mutmut_8': xǁRecipeSearchǁget__mutmut_8, 
        'xǁRecipeSearchǁget__mutmut_9': xǁRecipeSearchǁget__mutmut_9, 
        'xǁRecipeSearchǁget__mutmut_10': xǁRecipeSearchǁget__mutmut_10, 
        'xǁRecipeSearchǁget__mutmut_11': xǁRecipeSearchǁget__mutmut_11, 
        'xǁRecipeSearchǁget__mutmut_12': xǁRecipeSearchǁget__mutmut_12, 
        'xǁRecipeSearchǁget__mutmut_13': xǁRecipeSearchǁget__mutmut_13, 
        'xǁRecipeSearchǁget__mutmut_14': xǁRecipeSearchǁget__mutmut_14, 
        'xǁRecipeSearchǁget__mutmut_15': xǁRecipeSearchǁget__mutmut_15, 
        'xǁRecipeSearchǁget__mutmut_16': xǁRecipeSearchǁget__mutmut_16, 
        'xǁRecipeSearchǁget__mutmut_17': xǁRecipeSearchǁget__mutmut_17, 
        'xǁRecipeSearchǁget__mutmut_18': xǁRecipeSearchǁget__mutmut_18, 
        'xǁRecipeSearchǁget__mutmut_19': xǁRecipeSearchǁget__mutmut_19, 
        'xǁRecipeSearchǁget__mutmut_20': xǁRecipeSearchǁget__mutmut_20, 
        'xǁRecipeSearchǁget__mutmut_21': xǁRecipeSearchǁget__mutmut_21, 
        'xǁRecipeSearchǁget__mutmut_22': xǁRecipeSearchǁget__mutmut_22, 
        'xǁRecipeSearchǁget__mutmut_23': xǁRecipeSearchǁget__mutmut_23, 
        'xǁRecipeSearchǁget__mutmut_24': xǁRecipeSearchǁget__mutmut_24, 
        'xǁRecipeSearchǁget__mutmut_25': xǁRecipeSearchǁget__mutmut_25, 
        'xǁRecipeSearchǁget__mutmut_26': xǁRecipeSearchǁget__mutmut_26, 
        'xǁRecipeSearchǁget__mutmut_27': xǁRecipeSearchǁget__mutmut_27, 
        'xǁRecipeSearchǁget__mutmut_28': xǁRecipeSearchǁget__mutmut_28, 
        'xǁRecipeSearchǁget__mutmut_29': xǁRecipeSearchǁget__mutmut_29, 
        'xǁRecipeSearchǁget__mutmut_30': xǁRecipeSearchǁget__mutmut_30, 
        'xǁRecipeSearchǁget__mutmut_31': xǁRecipeSearchǁget__mutmut_31, 
        'xǁRecipeSearchǁget__mutmut_32': xǁRecipeSearchǁget__mutmut_32, 
        'xǁRecipeSearchǁget__mutmut_33': xǁRecipeSearchǁget__mutmut_33, 
        'xǁRecipeSearchǁget__mutmut_34': xǁRecipeSearchǁget__mutmut_34, 
        'xǁRecipeSearchǁget__mutmut_35': xǁRecipeSearchǁget__mutmut_35, 
        'xǁRecipeSearchǁget__mutmut_36': xǁRecipeSearchǁget__mutmut_36, 
        'xǁRecipeSearchǁget__mutmut_37': xǁRecipeSearchǁget__mutmut_37, 
        'xǁRecipeSearchǁget__mutmut_38': xǁRecipeSearchǁget__mutmut_38, 
        'xǁRecipeSearchǁget__mutmut_39': xǁRecipeSearchǁget__mutmut_39, 
        'xǁRecipeSearchǁget__mutmut_40': xǁRecipeSearchǁget__mutmut_40, 
        'xǁRecipeSearchǁget__mutmut_41': xǁRecipeSearchǁget__mutmut_41, 
        'xǁRecipeSearchǁget__mutmut_42': xǁRecipeSearchǁget__mutmut_42, 
        'xǁRecipeSearchǁget__mutmut_43': xǁRecipeSearchǁget__mutmut_43, 
        'xǁRecipeSearchǁget__mutmut_44': xǁRecipeSearchǁget__mutmut_44, 
        'xǁRecipeSearchǁget__mutmut_45': xǁRecipeSearchǁget__mutmut_45, 
        'xǁRecipeSearchǁget__mutmut_46': xǁRecipeSearchǁget__mutmut_46, 
        'xǁRecipeSearchǁget__mutmut_47': xǁRecipeSearchǁget__mutmut_47, 
        'xǁRecipeSearchǁget__mutmut_48': xǁRecipeSearchǁget__mutmut_48, 
        'xǁRecipeSearchǁget__mutmut_49': xǁRecipeSearchǁget__mutmut_49, 
        'xǁRecipeSearchǁget__mutmut_50': xǁRecipeSearchǁget__mutmut_50, 
        'xǁRecipeSearchǁget__mutmut_51': xǁRecipeSearchǁget__mutmut_51, 
        'xǁRecipeSearchǁget__mutmut_52': xǁRecipeSearchǁget__mutmut_52, 
        'xǁRecipeSearchǁget__mutmut_53': xǁRecipeSearchǁget__mutmut_53, 
        'xǁRecipeSearchǁget__mutmut_54': xǁRecipeSearchǁget__mutmut_54, 
        'xǁRecipeSearchǁget__mutmut_55': xǁRecipeSearchǁget__mutmut_55, 
        'xǁRecipeSearchǁget__mutmut_56': xǁRecipeSearchǁget__mutmut_56, 
        'xǁRecipeSearchǁget__mutmut_57': xǁRecipeSearchǁget__mutmut_57, 
        'xǁRecipeSearchǁget__mutmut_58': xǁRecipeSearchǁget__mutmut_58, 
        'xǁRecipeSearchǁget__mutmut_59': xǁRecipeSearchǁget__mutmut_59, 
        'xǁRecipeSearchǁget__mutmut_60': xǁRecipeSearchǁget__mutmut_60, 
        'xǁRecipeSearchǁget__mutmut_61': xǁRecipeSearchǁget__mutmut_61, 
        'xǁRecipeSearchǁget__mutmut_62': xǁRecipeSearchǁget__mutmut_62
    }

    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeSearchǁget__mutmut_orig"), object.__getattribute__(self, "xǁRecipeSearchǁget__mutmut_mutants"), *args, **kwargs)
        return result 

    get.__signature__ = _mutmut_signature(xǁRecipeSearchǁget__mutmut_orig)
    xǁRecipeSearchǁget__mutmut_orig.__name__ = 'xǁRecipeSearchǁget'


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
    def xǁGetPreferencesǁget__mutmut_orig(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('name', flat=True))
            blacklist = list(user_preference.blacklist.values_list('name', flat=True))
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})
    def xǁGetPreferencesǁget__mutmut_1(self, request):
        if request.user.is_authenticated:
            user_preference, _ = None
            whitelist = list(user_preference.whitelist.values_list('name', flat=True))
            blacklist = list(user_preference.blacklist.values_list('name', flat=True))
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})
    def xǁGetPreferencesǁget__mutmut_2(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('XXnameXX', flat=True))
            blacklist = list(user_preference.blacklist.values_list('name', flat=True))
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})
    def xǁGetPreferencesǁget__mutmut_3(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('name', flat=False))
            blacklist = list(user_preference.blacklist.values_list('name', flat=True))
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})
    def xǁGetPreferencesǁget__mutmut_4(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('name',))
            blacklist = list(user_preference.blacklist.values_list('name', flat=True))
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})
    def xǁGetPreferencesǁget__mutmut_5(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = None
            blacklist = list(user_preference.blacklist.values_list('name', flat=True))
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})
    def xǁGetPreferencesǁget__mutmut_6(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('name', flat=True))
            blacklist = list(user_preference.blacklist.values_list('XXnameXX', flat=True))
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})
    def xǁGetPreferencesǁget__mutmut_7(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('name', flat=True))
            blacklist = list(user_preference.blacklist.values_list('name', flat=False))
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})
    def xǁGetPreferencesǁget__mutmut_8(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('name', flat=True))
            blacklist = list(user_preference.blacklist.values_list('name',))
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})
    def xǁGetPreferencesǁget__mutmut_9(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('name', flat=True))
            blacklist = None
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})
    def xǁGetPreferencesǁget__mutmut_10(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('name', flat=True))
            blacklist = list(user_preference.blacklist.values_list('name', flat=True))
            return JsonResponse({'XXwhitelistXX': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})
    def xǁGetPreferencesǁget__mutmut_11(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('name', flat=True))
            blacklist = list(user_preference.blacklist.values_list('name', flat=True))
            return JsonResponse({'whitelist': whitelist, 'XXblacklistXX': blacklist})
        return JsonResponse({'whitelist': [], 'blacklist': []})
    def xǁGetPreferencesǁget__mutmut_12(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('name', flat=True))
            blacklist = list(user_preference.blacklist.values_list('name', flat=True))
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'XXwhitelistXX': [], 'blacklist': []})
    def xǁGetPreferencesǁget__mutmut_13(self, request):
        if request.user.is_authenticated:
            user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
            whitelist = list(user_preference.whitelist.values_list('name', flat=True))
            blacklist = list(user_preference.blacklist.values_list('name', flat=True))
            return JsonResponse({'whitelist': whitelist, 'blacklist': blacklist})
        return JsonResponse({'whitelist': [], 'XXblacklistXX': []})

    xǁGetPreferencesǁget__mutmut_mutants = {
    'xǁGetPreferencesǁget__mutmut_1': xǁGetPreferencesǁget__mutmut_1, 
        'xǁGetPreferencesǁget__mutmut_2': xǁGetPreferencesǁget__mutmut_2, 
        'xǁGetPreferencesǁget__mutmut_3': xǁGetPreferencesǁget__mutmut_3, 
        'xǁGetPreferencesǁget__mutmut_4': xǁGetPreferencesǁget__mutmut_4, 
        'xǁGetPreferencesǁget__mutmut_5': xǁGetPreferencesǁget__mutmut_5, 
        'xǁGetPreferencesǁget__mutmut_6': xǁGetPreferencesǁget__mutmut_6, 
        'xǁGetPreferencesǁget__mutmut_7': xǁGetPreferencesǁget__mutmut_7, 
        'xǁGetPreferencesǁget__mutmut_8': xǁGetPreferencesǁget__mutmut_8, 
        'xǁGetPreferencesǁget__mutmut_9': xǁGetPreferencesǁget__mutmut_9, 
        'xǁGetPreferencesǁget__mutmut_10': xǁGetPreferencesǁget__mutmut_10, 
        'xǁGetPreferencesǁget__mutmut_11': xǁGetPreferencesǁget__mutmut_11, 
        'xǁGetPreferencesǁget__mutmut_12': xǁGetPreferencesǁget__mutmut_12, 
        'xǁGetPreferencesǁget__mutmut_13': xǁGetPreferencesǁget__mutmut_13
    }

    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGetPreferencesǁget__mutmut_orig"), object.__getattribute__(self, "xǁGetPreferencesǁget__mutmut_mutants"), *args, **kwargs)
        return result 

    get.__signature__ = _mutmut_signature(xǁGetPreferencesǁget__mutmut_orig)
    xǁGetPreferencesǁget__mutmut_orig.__name__ = 'xǁGetPreferencesǁget'



class RecipeDetailView(View):
    def xǁRecipeDetailViewǁget__mutmut_orig(self, request, id):
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
    def xǁRecipeDetailViewǁget__mutmut_1(self, request, id):
        recipe = get_object_or_404(None, id=id)

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
    def xǁRecipeDetailViewǁget__mutmut_2(self, request, id):
        recipe = get_object_or_404(Recipe, id=None)

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
    def xǁRecipeDetailViewǁget__mutmut_3(self, request, id):
        recipe = get_object_or_404( id=id)

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
    def xǁRecipeDetailViewǁget__mutmut_4(self, request, id):
        recipe = get_object_or_404(Recipe,)

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
    def xǁRecipeDetailViewǁget__mutmut_5(self, request, id):
        recipe = None

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
    def xǁRecipeDetailViewǁget__mutmut_6(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, None)

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
    def xǁRecipeDetailViewǁget__mutmut_7(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user,)

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
    def xǁRecipeDetailViewǁget__mutmut_8(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = None

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
    def xǁRecipeDetailViewǁget__mutmut_9(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = re.sub(r'XX\d+\.\s*XX', '', recipe.instructions.strip())

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
    def xǁRecipeDetailViewǁget__mutmut_10(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = re.sub(r'\d+\.\s*', 'XXXX', recipe.instructions.strip())

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
    def xǁRecipeDetailViewǁget__mutmut_11(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = None

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
    def xǁRecipeDetailViewǁget__mutmut_12(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = re.sub(r'\d+\.\s*', '', recipe.instructions.strip())

        # Split instructions by periods
        instructions_list = re.split(r'XX\.\s+XX', instructions)

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
    def xǁRecipeDetailViewǁget__mutmut_13(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = re.sub(r'\d+\.\s*', '', recipe.instructions.strip())

        # Split instructions by periods
        instructions_list = re.split(r'\.\s+', None)

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
    def xǁRecipeDetailViewǁget__mutmut_14(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = re.sub(r'\d+\.\s*', '', recipe.instructions.strip())

        # Split instructions by periods
        instructions_list = re.split(r'\.\s+',)

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
    def xǁRecipeDetailViewǁget__mutmut_15(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = re.sub(r'\d+\.\s*', '', recipe.instructions.strip())

        # Split instructions by periods
        instructions_list = None

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
    def xǁRecipeDetailViewǁget__mutmut_16(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = re.sub(r'\d+\.\s*', '', recipe.instructions.strip())

        # Split instructions by periods
        instructions_list = re.split(r'\.\s+', instructions)

        # add a period to the end of each instruction if it doesn't already have one
        instructions_list = [instruction - '.' if not instruction.endswith('.') else instruction for instruction in instructions_list]

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
    def xǁRecipeDetailViewǁget__mutmut_17(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = re.sub(r'\d+\.\s*', '', recipe.instructions.strip())

        # Split instructions by periods
        instructions_list = re.split(r'\.\s+', instructions)

        # add a period to the end of each instruction if it doesn't already have one
        instructions_list = [instruction + 'XX.XX' if not instruction.endswith('.') else instruction for instruction in instructions_list]

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
    def xǁRecipeDetailViewǁget__mutmut_18(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = re.sub(r'\d+\.\s*', '', recipe.instructions.strip())

        # Split instructions by periods
        instructions_list = re.split(r'\.\s+', instructions)

        # add a period to the end of each instruction if it doesn't already have one
        instructions_list = [instruction + '.' if  instruction.endswith('.') else instruction for instruction in instructions_list]

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
    def xǁRecipeDetailViewǁget__mutmut_19(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = re.sub(r'\d+\.\s*', '', recipe.instructions.strip())

        # Split instructions by periods
        instructions_list = re.split(r'\.\s+', instructions)

        # add a period to the end of each instruction if it doesn't already have one
        instructions_list = [instruction + '.' if not instruction.endswith('XX.XX') else instruction for instruction in instructions_list]

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
    def xǁRecipeDetailViewǁget__mutmut_20(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)

        # Set favorite status for authenticated users
        is_favorited = self._is_favorited_by_user(request.user, recipe)

        # Remove numbered steps from instructions
        instructions = re.sub(r'\d+\.\s*', '', recipe.instructions.strip())

        # Split instructions by periods
        instructions_list = re.split(r'\.\s+', instructions)

        # add a period to the end of each instruction if it doesn't already have one
        instructions_list = None

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
    def xǁRecipeDetailViewǁget__mutmut_21(self, request, id):
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
        instructions_list = None
        
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
    def xǁRecipeDetailViewǁget__mutmut_22(self, request, id):
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
        user_rating = ""
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
    def xǁRecipeDetailViewǁget__mutmut_23(self, request, id):
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
        user_review = ""
        
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
    def xǁRecipeDetailViewǁget__mutmut_24(self, request, id):
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
                rating = Rating.objects.get(user=request.user, recipe=None)
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
    def xǁRecipeDetailViewǁget__mutmut_25(self, request, id):
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
                rating = Rating.objects.get( recipe=recipe)
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
    def xǁRecipeDetailViewǁget__mutmut_26(self, request, id):
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
                rating = Rating.objects.get(user=request.user,)
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
    def xǁRecipeDetailViewǁget__mutmut_27(self, request, id):
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
                rating = None
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
    def xǁRecipeDetailViewǁget__mutmut_28(self, request, id):
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
                user_rating = None
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
    def xǁRecipeDetailViewǁget__mutmut_29(self, request, id):
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
                user_review = None 
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
    def xǁRecipeDetailViewǁget__mutmut_30(self, request, id):
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
                user_rating = ""
                user_review = None

        context = {
            'recipe': recipe,
            'is_favorited': is_favorited,
            'instructions_list': instructions_list,
            'user_rating': user_rating,
            'user_review': user_review,
        }
        return render(request, 'cookapp/recipe_detail.html', context)
    def xǁRecipeDetailViewǁget__mutmut_31(self, request, id):
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
                user_review = ""

        context = {
            'recipe': recipe,
            'is_favorited': is_favorited,
            'instructions_list': instructions_list,
            'user_rating': user_rating,
            'user_review': user_review,
        }
        return render(request, 'cookapp/recipe_detail.html', context)
    def xǁRecipeDetailViewǁget__mutmut_32(self, request, id):
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
            'XXrecipeXX': recipe,
            'is_favorited': is_favorited,
            'instructions_list': instructions_list,
            'user_rating': user_rating,
            'user_review': user_review,
        }
        return render(request, 'cookapp/recipe_detail.html', context)
    def xǁRecipeDetailViewǁget__mutmut_33(self, request, id):
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
            'XXis_favoritedXX': is_favorited,
            'instructions_list': instructions_list,
            'user_rating': user_rating,
            'user_review': user_review,
        }
        return render(request, 'cookapp/recipe_detail.html', context)
    def xǁRecipeDetailViewǁget__mutmut_34(self, request, id):
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
            'XXinstructions_listXX': instructions_list,
            'user_rating': user_rating,
            'user_review': user_review,
        }
        return render(request, 'cookapp/recipe_detail.html', context)
    def xǁRecipeDetailViewǁget__mutmut_35(self, request, id):
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
            'XXuser_ratingXX': user_rating,
            'user_review': user_review,
        }
        return render(request, 'cookapp/recipe_detail.html', context)
    def xǁRecipeDetailViewǁget__mutmut_36(self, request, id):
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
            'XXuser_reviewXX': user_review,
        }
        return render(request, 'cookapp/recipe_detail.html', context)
    def xǁRecipeDetailViewǁget__mutmut_37(self, request, id):
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

        context = None
        return render(request, 'cookapp/recipe_detail.html', context)
    def xǁRecipeDetailViewǁget__mutmut_38(self, request, id):
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
        return render(None, 'cookapp/recipe_detail.html', context)
    def xǁRecipeDetailViewǁget__mutmut_39(self, request, id):
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
        return render(request, 'XXcookapp/recipe_detail.htmlXX', context)
    def xǁRecipeDetailViewǁget__mutmut_40(self, request, id):
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
        return render(request, 'cookapp/recipe_detail.html', None)
    def xǁRecipeDetailViewǁget__mutmut_41(self, request, id):
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
        return render( 'cookapp/recipe_detail.html', context)
    def xǁRecipeDetailViewǁget__mutmut_42(self, request, id):
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
        return render(request, 'cookapp/recipe_detail.html',)

    xǁRecipeDetailViewǁget__mutmut_mutants = {
    'xǁRecipeDetailViewǁget__mutmut_1': xǁRecipeDetailViewǁget__mutmut_1, 
        'xǁRecipeDetailViewǁget__mutmut_2': xǁRecipeDetailViewǁget__mutmut_2, 
        'xǁRecipeDetailViewǁget__mutmut_3': xǁRecipeDetailViewǁget__mutmut_3, 
        'xǁRecipeDetailViewǁget__mutmut_4': xǁRecipeDetailViewǁget__mutmut_4, 
        'xǁRecipeDetailViewǁget__mutmut_5': xǁRecipeDetailViewǁget__mutmut_5, 
        'xǁRecipeDetailViewǁget__mutmut_6': xǁRecipeDetailViewǁget__mutmut_6, 
        'xǁRecipeDetailViewǁget__mutmut_7': xǁRecipeDetailViewǁget__mutmut_7, 
        'xǁRecipeDetailViewǁget__mutmut_8': xǁRecipeDetailViewǁget__mutmut_8, 
        'xǁRecipeDetailViewǁget__mutmut_9': xǁRecipeDetailViewǁget__mutmut_9, 
        'xǁRecipeDetailViewǁget__mutmut_10': xǁRecipeDetailViewǁget__mutmut_10, 
        'xǁRecipeDetailViewǁget__mutmut_11': xǁRecipeDetailViewǁget__mutmut_11, 
        'xǁRecipeDetailViewǁget__mutmut_12': xǁRecipeDetailViewǁget__mutmut_12, 
        'xǁRecipeDetailViewǁget__mutmut_13': xǁRecipeDetailViewǁget__mutmut_13, 
        'xǁRecipeDetailViewǁget__mutmut_14': xǁRecipeDetailViewǁget__mutmut_14, 
        'xǁRecipeDetailViewǁget__mutmut_15': xǁRecipeDetailViewǁget__mutmut_15, 
        'xǁRecipeDetailViewǁget__mutmut_16': xǁRecipeDetailViewǁget__mutmut_16, 
        'xǁRecipeDetailViewǁget__mutmut_17': xǁRecipeDetailViewǁget__mutmut_17, 
        'xǁRecipeDetailViewǁget__mutmut_18': xǁRecipeDetailViewǁget__mutmut_18, 
        'xǁRecipeDetailViewǁget__mutmut_19': xǁRecipeDetailViewǁget__mutmut_19, 
        'xǁRecipeDetailViewǁget__mutmut_20': xǁRecipeDetailViewǁget__mutmut_20, 
        'xǁRecipeDetailViewǁget__mutmut_21': xǁRecipeDetailViewǁget__mutmut_21, 
        'xǁRecipeDetailViewǁget__mutmut_22': xǁRecipeDetailViewǁget__mutmut_22, 
        'xǁRecipeDetailViewǁget__mutmut_23': xǁRecipeDetailViewǁget__mutmut_23, 
        'xǁRecipeDetailViewǁget__mutmut_24': xǁRecipeDetailViewǁget__mutmut_24, 
        'xǁRecipeDetailViewǁget__mutmut_25': xǁRecipeDetailViewǁget__mutmut_25, 
        'xǁRecipeDetailViewǁget__mutmut_26': xǁRecipeDetailViewǁget__mutmut_26, 
        'xǁRecipeDetailViewǁget__mutmut_27': xǁRecipeDetailViewǁget__mutmut_27, 
        'xǁRecipeDetailViewǁget__mutmut_28': xǁRecipeDetailViewǁget__mutmut_28, 
        'xǁRecipeDetailViewǁget__mutmut_29': xǁRecipeDetailViewǁget__mutmut_29, 
        'xǁRecipeDetailViewǁget__mutmut_30': xǁRecipeDetailViewǁget__mutmut_30, 
        'xǁRecipeDetailViewǁget__mutmut_31': xǁRecipeDetailViewǁget__mutmut_31, 
        'xǁRecipeDetailViewǁget__mutmut_32': xǁRecipeDetailViewǁget__mutmut_32, 
        'xǁRecipeDetailViewǁget__mutmut_33': xǁRecipeDetailViewǁget__mutmut_33, 
        'xǁRecipeDetailViewǁget__mutmut_34': xǁRecipeDetailViewǁget__mutmut_34, 
        'xǁRecipeDetailViewǁget__mutmut_35': xǁRecipeDetailViewǁget__mutmut_35, 
        'xǁRecipeDetailViewǁget__mutmut_36': xǁRecipeDetailViewǁget__mutmut_36, 
        'xǁRecipeDetailViewǁget__mutmut_37': xǁRecipeDetailViewǁget__mutmut_37, 
        'xǁRecipeDetailViewǁget__mutmut_38': xǁRecipeDetailViewǁget__mutmut_38, 
        'xǁRecipeDetailViewǁget__mutmut_39': xǁRecipeDetailViewǁget__mutmut_39, 
        'xǁRecipeDetailViewǁget__mutmut_40': xǁRecipeDetailViewǁget__mutmut_40, 
        'xǁRecipeDetailViewǁget__mutmut_41': xǁRecipeDetailViewǁget__mutmut_41, 
        'xǁRecipeDetailViewǁget__mutmut_42': xǁRecipeDetailViewǁget__mutmut_42
    }

    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeDetailViewǁget__mutmut_orig"), object.__getattribute__(self, "xǁRecipeDetailViewǁget__mutmut_mutants"), *args, **kwargs)
        return result 

    get.__signature__ = _mutmut_signature(xǁRecipeDetailViewǁget__mutmut_orig)
    xǁRecipeDetailViewǁget__mutmut_orig.__name__ = 'xǁRecipeDetailViewǁget'



    def xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_orig(self, user, recipe):
        if user.is_authenticated:
            return FavoriteRecipe.objects.filter(user=user, recipe=recipe).exists()
        return False

    def xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_1(self, user, recipe):
        if user.is_authenticated:
            return FavoriteRecipe.objects.filter(user=None, recipe=recipe).exists()
        return False

    def xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_2(self, user, recipe):
        if user.is_authenticated:
            return FavoriteRecipe.objects.filter(user=user, recipe=None).exists()
        return False

    def xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_3(self, user, recipe):
        if user.is_authenticated:
            return FavoriteRecipe.objects.filter( recipe=recipe).exists()
        return False

    def xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_4(self, user, recipe):
        if user.is_authenticated:
            return FavoriteRecipe.objects.filter(user=user,).exists()
        return False

    def xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_5(self, user, recipe):
        if user.is_authenticated:
            return FavoriteRecipe.objects.filter(user=user, recipe=recipe).exists()
        return True

    xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_mutants = {
    'xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_1': xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_1, 
        'xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_2': xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_2, 
        'xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_3': xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_3, 
        'xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_4': xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_4, 
        'xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_5': xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_5
    }

    def _is_favorited_by_user(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_orig"), object.__getattribute__(self, "xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_mutants"), *args, **kwargs)
        return result 

    _is_favorited_by_user.__signature__ = _mutmut_signature(xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_orig)
    xǁRecipeDetailViewǁ_is_favorited_by_user__mutmut_orig.__name__ = 'xǁRecipeDetailViewǁ_is_favorited_by_user'



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
    def xǁReviewsViewǁget__mutmut_orig(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html', context)
    def xǁReviewsViewǁget__mutmut_1(self, request):
        reviews = Rating.objects.filter(review__isnull=True).select_related('recipe', 'user')
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html', context)
    def xǁReviewsViewǁget__mutmut_2(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('XXrecipeXX', 'user')
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html', context)
    def xǁReviewsViewǁget__mutmut_3(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'XXuserXX')
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html', context)
    def xǁReviewsViewǁget__mutmut_4(self, request):
        reviews = None
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html', context)
    def xǁReviewsViewǁget__mutmut_5(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        rating = Rating.objects.filter(review__isnull=True).select_related('recipe', 'user')
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html', context)
    def xǁReviewsViewǁget__mutmut_6(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        rating = Rating.objects.filter(review__isnull=False).select_related('XXrecipeXX', 'user')
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html', context)
    def xǁReviewsViewǁget__mutmut_7(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'XXuserXX')
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html', context)
    def xǁReviewsViewǁget__mutmut_8(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        rating = None
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html', context)
    def xǁReviewsViewǁget__mutmut_9(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        context = {
            'XXreviewsXX': reviews,
        }
        return render(request, 'cookapp/reviews.html', context)
    def xǁReviewsViewǁget__mutmut_10(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        context = None
        return render(request, 'cookapp/reviews.html', context)
    def xǁReviewsViewǁget__mutmut_11(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        context = {
            'reviews': reviews,
        }
        return render(None, 'cookapp/reviews.html', context)
    def xǁReviewsViewǁget__mutmut_12(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        context = {
            'reviews': reviews,
        }
        return render(request, 'XXcookapp/reviews.htmlXX', context)
    def xǁReviewsViewǁget__mutmut_13(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html', None)
    def xǁReviewsViewǁget__mutmut_14(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        context = {
            'reviews': reviews,
        }
        return render( 'cookapp/reviews.html', context)
    def xǁReviewsViewǁget__mutmut_15(self, request):
        reviews = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        rating = Rating.objects.filter(review__isnull=False).select_related('recipe', 'user')
        context = {
            'reviews': reviews,
        }
        return render(request, 'cookapp/reviews.html',)

    xǁReviewsViewǁget__mutmut_mutants = {
    'xǁReviewsViewǁget__mutmut_1': xǁReviewsViewǁget__mutmut_1, 
        'xǁReviewsViewǁget__mutmut_2': xǁReviewsViewǁget__mutmut_2, 
        'xǁReviewsViewǁget__mutmut_3': xǁReviewsViewǁget__mutmut_3, 
        'xǁReviewsViewǁget__mutmut_4': xǁReviewsViewǁget__mutmut_4, 
        'xǁReviewsViewǁget__mutmut_5': xǁReviewsViewǁget__mutmut_5, 
        'xǁReviewsViewǁget__mutmut_6': xǁReviewsViewǁget__mutmut_6, 
        'xǁReviewsViewǁget__mutmut_7': xǁReviewsViewǁget__mutmut_7, 
        'xǁReviewsViewǁget__mutmut_8': xǁReviewsViewǁget__mutmut_8, 
        'xǁReviewsViewǁget__mutmut_9': xǁReviewsViewǁget__mutmut_9, 
        'xǁReviewsViewǁget__mutmut_10': xǁReviewsViewǁget__mutmut_10, 
        'xǁReviewsViewǁget__mutmut_11': xǁReviewsViewǁget__mutmut_11, 
        'xǁReviewsViewǁget__mutmut_12': xǁReviewsViewǁget__mutmut_12, 
        'xǁReviewsViewǁget__mutmut_13': xǁReviewsViewǁget__mutmut_13, 
        'xǁReviewsViewǁget__mutmut_14': xǁReviewsViewǁget__mutmut_14, 
        'xǁReviewsViewǁget__mutmut_15': xǁReviewsViewǁget__mutmut_15
    }

    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁReviewsViewǁget__mutmut_orig"), object.__getattribute__(self, "xǁReviewsViewǁget__mutmut_mutants"), *args, **kwargs)
        return result 

    get.__signature__ = _mutmut_signature(xǁReviewsViewǁget__mutmut_orig)
    xǁReviewsViewǁget__mutmut_orig.__name__ = 'xǁReviewsViewǁget'


    
class MealPlanView(View):
    def xǁMealPlanViewǁget__mutmut_orig(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_1(self, request):
        days = ["XXMondayXX", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_2(self, request):
        days = ["Monday", "XXTuesdayXX", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_3(self, request):
        days = ["Monday", "Tuesday", "XXWednesdayXX", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_4(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "XXThursdayXX", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_5(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "XXFridayXX", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_6(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "XXSaturdayXX", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_7(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "XXSundayXX"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_8(self, request):
        days = None
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_9(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["XXBreakfastXX", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_10(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "XXLunchXX", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_11(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "XXSnackXX", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_12(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "XXDinnerXX"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_13(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = None
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_14(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'XXdaysXX': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_15(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'XXmealsXX': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_16(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = None
        return render(request, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_17(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(None, 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_18(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'XXcookapp/mealPlanner.htmlXX', context)
    def xǁMealPlanViewǁget__mutmut_19(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html', None)
    def xǁMealPlanViewǁget__mutmut_20(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render( 'cookapp/mealPlanner.html', context)
    def xǁMealPlanViewǁget__mutmut_21(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Snack", "Dinner"]
        context = {
            'days': days,
            'meals': meals,
        }
        return render(request, 'cookapp/mealPlanner.html',)

    xǁMealPlanViewǁget__mutmut_mutants = {
    'xǁMealPlanViewǁget__mutmut_1': xǁMealPlanViewǁget__mutmut_1, 
        'xǁMealPlanViewǁget__mutmut_2': xǁMealPlanViewǁget__mutmut_2, 
        'xǁMealPlanViewǁget__mutmut_3': xǁMealPlanViewǁget__mutmut_3, 
        'xǁMealPlanViewǁget__mutmut_4': xǁMealPlanViewǁget__mutmut_4, 
        'xǁMealPlanViewǁget__mutmut_5': xǁMealPlanViewǁget__mutmut_5, 
        'xǁMealPlanViewǁget__mutmut_6': xǁMealPlanViewǁget__mutmut_6, 
        'xǁMealPlanViewǁget__mutmut_7': xǁMealPlanViewǁget__mutmut_7, 
        'xǁMealPlanViewǁget__mutmut_8': xǁMealPlanViewǁget__mutmut_8, 
        'xǁMealPlanViewǁget__mutmut_9': xǁMealPlanViewǁget__mutmut_9, 
        'xǁMealPlanViewǁget__mutmut_10': xǁMealPlanViewǁget__mutmut_10, 
        'xǁMealPlanViewǁget__mutmut_11': xǁMealPlanViewǁget__mutmut_11, 
        'xǁMealPlanViewǁget__mutmut_12': xǁMealPlanViewǁget__mutmut_12, 
        'xǁMealPlanViewǁget__mutmut_13': xǁMealPlanViewǁget__mutmut_13, 
        'xǁMealPlanViewǁget__mutmut_14': xǁMealPlanViewǁget__mutmut_14, 
        'xǁMealPlanViewǁget__mutmut_15': xǁMealPlanViewǁget__mutmut_15, 
        'xǁMealPlanViewǁget__mutmut_16': xǁMealPlanViewǁget__mutmut_16, 
        'xǁMealPlanViewǁget__mutmut_17': xǁMealPlanViewǁget__mutmut_17, 
        'xǁMealPlanViewǁget__mutmut_18': xǁMealPlanViewǁget__mutmut_18, 
        'xǁMealPlanViewǁget__mutmut_19': xǁMealPlanViewǁget__mutmut_19, 
        'xǁMealPlanViewǁget__mutmut_20': xǁMealPlanViewǁget__mutmut_20, 
        'xǁMealPlanViewǁget__mutmut_21': xǁMealPlanViewǁget__mutmut_21
    }

    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMealPlanViewǁget__mutmut_orig"), object.__getattribute__(self, "xǁMealPlanViewǁget__mutmut_mutants"), *args, **kwargs)
        return result 

    get.__signature__ = _mutmut_signature(xǁMealPlanViewǁget__mutmut_orig)
    xǁMealPlanViewǁget__mutmut_orig.__name__ = 'xǁMealPlanViewǁget'



def x_toggle_favorite__mutmut_orig(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

def x_toggle_favorite__mutmut_1(request, recipe_id):
    if request.method != 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

def x_toggle_favorite__mutmut_2(request, recipe_id):
    if request.method == 'XXPOSTXX':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

def x_toggle_favorite__mutmut_3(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(None, id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

def x_toggle_favorite__mutmut_4(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=None)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

def x_toggle_favorite__mutmut_5(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404( id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

def x_toggle_favorite__mutmut_6(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe,)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

def x_toggle_favorite__mutmut_7(request, recipe_id):
    if request.method == 'POST':
        recipe = None
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

def x_toggle_favorite__mutmut_8(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=None)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

def x_toggle_favorite__mutmut_9(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create( recipe=recipe)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

def x_toggle_favorite__mutmut_10(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user,)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

def x_toggle_favorite__mutmut_11(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = None
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

def x_toggle_favorite__mutmut_12(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
        if  created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=recipe_id)

def x_toggle_favorite__mutmut_13(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('XXrecipe_detailXX', id=recipe_id)

def x_toggle_favorite__mutmut_14(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail', id=None)

def x_toggle_favorite__mutmut_15(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Check if the user already has this recipe as a favorite
        favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
        if not created:  # If it was not created, it means it already exists, so remove it
            favorite.delete()  # Remove from favorites
        # If created, it means it was added, so no action is needed.

    return redirect('recipe_detail',)

x_toggle_favorite__mutmut_mutants = {
'x_toggle_favorite__mutmut_1': x_toggle_favorite__mutmut_1, 
    'x_toggle_favorite__mutmut_2': x_toggle_favorite__mutmut_2, 
    'x_toggle_favorite__mutmut_3': x_toggle_favorite__mutmut_3, 
    'x_toggle_favorite__mutmut_4': x_toggle_favorite__mutmut_4, 
    'x_toggle_favorite__mutmut_5': x_toggle_favorite__mutmut_5, 
    'x_toggle_favorite__mutmut_6': x_toggle_favorite__mutmut_6, 
    'x_toggle_favorite__mutmut_7': x_toggle_favorite__mutmut_7, 
    'x_toggle_favorite__mutmut_8': x_toggle_favorite__mutmut_8, 
    'x_toggle_favorite__mutmut_9': x_toggle_favorite__mutmut_9, 
    'x_toggle_favorite__mutmut_10': x_toggle_favorite__mutmut_10, 
    'x_toggle_favorite__mutmut_11': x_toggle_favorite__mutmut_11, 
    'x_toggle_favorite__mutmut_12': x_toggle_favorite__mutmut_12, 
    'x_toggle_favorite__mutmut_13': x_toggle_favorite__mutmut_13, 
    'x_toggle_favorite__mutmut_14': x_toggle_favorite__mutmut_14, 
    'x_toggle_favorite__mutmut_15': x_toggle_favorite__mutmut_15
}

def toggle_favorite(*args, **kwargs):
    result = _mutmut_trampoline(x_toggle_favorite__mutmut_orig, x_toggle_favorite__mutmut_mutants, *args, **kwargs)
    return result 

toggle_favorite.__signature__ = _mutmut_signature(x_toggle_favorite__mutmut_orig)
x_toggle_favorite__mutmut_orig.__name__ = 'x_toggle_favorite'



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
    def xǁRecipeListViewǁget_queryset__mutmut_orig(self):
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_1(self):
        queryset = None
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_2(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('XXsortXX', 'name')  # Default to 'name' for A-Z sorting

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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_3(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'XXnameXX')  # Default to 'name' for A-Z sorting

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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_4(self):
        queryset = super().get_queryset()
        sort = None  # Default to 'name' for A-Z sorting

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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_5(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort != 'name_desc':
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_6(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'XXname_descXX':
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_7(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('XX-titleXX')
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_8(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = None
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_9(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort != 'rating':
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_10(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'XXratingXX':
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_11(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=1, then=Value(None)),
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_12(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When( then=Value(None)),
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_13(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=0,),
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_14(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=0, then=Value(None)),
                    default='XXaverage_ratingXX',
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_15(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=0, then=Value(None)),
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_16(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=0, then=Value(None)),
                    default='average_rating',
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_17(self):
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
            ).order_by('XX-rating_caseXX', '-average_rating', 'title')  # First by non-zero ratings, then by rating
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_18(self):
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
            ).order_by('-rating_case', 'XX-average_ratingXX', 'title')  # First by non-zero ratings, then by rating
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_19(self):
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
            ).order_by('-rating_case', '-average_rating', 'XXtitleXX')  # First by non-zero ratings, then by rating
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_20(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = None  # First by non-zero ratings, then by rating
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_21(self):
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
        elif sort != 'rating_asc':
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_22(self):
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
        elif sort == 'XXrating_ascXX':
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_23(self):
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
                    When(average_rating=1, then=Value(None)),
                    default='average_rating',
                    output_field=IntegerField(),
                )
            ).order_by('rating_case', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_24(self):
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
                    When( then=Value(None)),
                    default='average_rating',
                    output_field=IntegerField(),
                )
            ).order_by('rating_case', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_25(self):
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
                    When(average_rating=0,),
                    default='average_rating',
                    output_field=IntegerField(),
                )
            ).order_by('rating_case', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_26(self):
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
                    default='XXaverage_ratingXX',
                    output_field=IntegerField(),
                )
            ).order_by('rating_case', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_27(self):
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
                    output_field=IntegerField(),
                )
            ).order_by('rating_case', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_28(self):
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
                )
            ).order_by('rating_case', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_29(self):
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
            ).order_by('XXrating_caseXX', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_30(self):
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
            ).order_by('rating_case', 'XXaverage_ratingXX', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_31(self):
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
            ).order_by('rating_case', 'average_rating', 'XXtitleXX')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_32(self):
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
            queryset = None  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_33(self):
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
            queryset = queryset.order_by('XXtitleXX')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_34(self):
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
            queryset = None

        return queryset

    xǁRecipeListViewǁget_queryset__mutmut_mutants = {
    'xǁRecipeListViewǁget_queryset__mutmut_1': xǁRecipeListViewǁget_queryset__mutmut_1, 
        'xǁRecipeListViewǁget_queryset__mutmut_2': xǁRecipeListViewǁget_queryset__mutmut_2, 
        'xǁRecipeListViewǁget_queryset__mutmut_3': xǁRecipeListViewǁget_queryset__mutmut_3, 
        'xǁRecipeListViewǁget_queryset__mutmut_4': xǁRecipeListViewǁget_queryset__mutmut_4, 
        'xǁRecipeListViewǁget_queryset__mutmut_5': xǁRecipeListViewǁget_queryset__mutmut_5, 
        'xǁRecipeListViewǁget_queryset__mutmut_6': xǁRecipeListViewǁget_queryset__mutmut_6, 
        'xǁRecipeListViewǁget_queryset__mutmut_7': xǁRecipeListViewǁget_queryset__mutmut_7, 
        'xǁRecipeListViewǁget_queryset__mutmut_8': xǁRecipeListViewǁget_queryset__mutmut_8, 
        'xǁRecipeListViewǁget_queryset__mutmut_9': xǁRecipeListViewǁget_queryset__mutmut_9, 
        'xǁRecipeListViewǁget_queryset__mutmut_10': xǁRecipeListViewǁget_queryset__mutmut_10, 
        'xǁRecipeListViewǁget_queryset__mutmut_11': xǁRecipeListViewǁget_queryset__mutmut_11, 
        'xǁRecipeListViewǁget_queryset__mutmut_12': xǁRecipeListViewǁget_queryset__mutmut_12, 
        'xǁRecipeListViewǁget_queryset__mutmut_13': xǁRecipeListViewǁget_queryset__mutmut_13, 
        'xǁRecipeListViewǁget_queryset__mutmut_14': xǁRecipeListViewǁget_queryset__mutmut_14, 
        'xǁRecipeListViewǁget_queryset__mutmut_15': xǁRecipeListViewǁget_queryset__mutmut_15, 
        'xǁRecipeListViewǁget_queryset__mutmut_16': xǁRecipeListViewǁget_queryset__mutmut_16, 
        'xǁRecipeListViewǁget_queryset__mutmut_17': xǁRecipeListViewǁget_queryset__mutmut_17, 
        'xǁRecipeListViewǁget_queryset__mutmut_18': xǁRecipeListViewǁget_queryset__mutmut_18, 
        'xǁRecipeListViewǁget_queryset__mutmut_19': xǁRecipeListViewǁget_queryset__mutmut_19, 
        'xǁRecipeListViewǁget_queryset__mutmut_20': xǁRecipeListViewǁget_queryset__mutmut_20, 
        'xǁRecipeListViewǁget_queryset__mutmut_21': xǁRecipeListViewǁget_queryset__mutmut_21, 
        'xǁRecipeListViewǁget_queryset__mutmut_22': xǁRecipeListViewǁget_queryset__mutmut_22, 
        'xǁRecipeListViewǁget_queryset__mutmut_23': xǁRecipeListViewǁget_queryset__mutmut_23, 
        'xǁRecipeListViewǁget_queryset__mutmut_24': xǁRecipeListViewǁget_queryset__mutmut_24, 
        'xǁRecipeListViewǁget_queryset__mutmut_25': xǁRecipeListViewǁget_queryset__mutmut_25, 
        'xǁRecipeListViewǁget_queryset__mutmut_26': xǁRecipeListViewǁget_queryset__mutmut_26, 
        'xǁRecipeListViewǁget_queryset__mutmut_27': xǁRecipeListViewǁget_queryset__mutmut_27, 
        'xǁRecipeListViewǁget_queryset__mutmut_28': xǁRecipeListViewǁget_queryset__mutmut_28, 
        'xǁRecipeListViewǁget_queryset__mutmut_29': xǁRecipeListViewǁget_queryset__mutmut_29, 
        'xǁRecipeListViewǁget_queryset__mutmut_30': xǁRecipeListViewǁget_queryset__mutmut_30, 
        'xǁRecipeListViewǁget_queryset__mutmut_31': xǁRecipeListViewǁget_queryset__mutmut_31, 
        'xǁRecipeListViewǁget_queryset__mutmut_32': xǁRecipeListViewǁget_queryset__mutmut_32, 
        'xǁRecipeListViewǁget_queryset__mutmut_33': xǁRecipeListViewǁget_queryset__mutmut_33, 
        'xǁRecipeListViewǁget_queryset__mutmut_34': xǁRecipeListViewǁget_queryset__mutmut_34
    }

    def get_queryset(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeListViewǁget_queryset__mutmut_orig"), object.__getattribute__(self, "xǁRecipeListViewǁget_queryset__mutmut_mutants"), *args, **kwargs)
        return result 

    get_queryset.__signature__ = _mutmut_signature(xǁRecipeListViewǁget_queryset__mutmut_orig)
    xǁRecipeListViewǁget_queryset__mutmut_orig.__name__ = 'xǁRecipeListViewǁget_queryset'




class RedirectToDetailView(View):
    def xǁRedirectToDetailViewǁpost__mutmut_orig(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_1(self, request):
        # Collect data from POST request
        data = None
        search_term = data.get('term', 'No input')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_2(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('XXtermXX', 'No input')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_3(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'XXNo inputXX')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_4(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = None
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_5(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = data.get('XXwhitelistXX', ['No input'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_6(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = data.get('whitelist', ['XXNo inputXX'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_7(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = None
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_8(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('XXblacklistXX', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_9(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('blacklist', ['XXNo inputXX'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_10(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = None

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_11(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"XX&whitelist=XX".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_12(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(None)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_13(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"XX&blacklist=XX".join(blacklist)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_14(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(None)}'
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_15(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = None
        return JsonResponse({'redirect_url': redirect_url})
    def xǁRedirectToDetailViewǁpost__mutmut_16(self, request):
        # Collect data from POST request
        data = json.loads(request.body)
        search_term = data.get('term', 'No input')
        whitelist = data.get('whitelist', ['No input'])
        blacklist = data.get('blacklist', ['No input'])

        # Redirect to the detail view with the arguments
        redirect_url = f'/simple-recipe-detail/?term={search_term}&whitelist={"&whitelist=".join(whitelist)}&blacklist={"&blacklist=".join(blacklist)}'
        return JsonResponse({'XXredirect_urlXX': redirect_url})

    xǁRedirectToDetailViewǁpost__mutmut_mutants = {
    'xǁRedirectToDetailViewǁpost__mutmut_1': xǁRedirectToDetailViewǁpost__mutmut_1, 
        'xǁRedirectToDetailViewǁpost__mutmut_2': xǁRedirectToDetailViewǁpost__mutmut_2, 
        'xǁRedirectToDetailViewǁpost__mutmut_3': xǁRedirectToDetailViewǁpost__mutmut_3, 
        'xǁRedirectToDetailViewǁpost__mutmut_4': xǁRedirectToDetailViewǁpost__mutmut_4, 
        'xǁRedirectToDetailViewǁpost__mutmut_5': xǁRedirectToDetailViewǁpost__mutmut_5, 
        'xǁRedirectToDetailViewǁpost__mutmut_6': xǁRedirectToDetailViewǁpost__mutmut_6, 
        'xǁRedirectToDetailViewǁpost__mutmut_7': xǁRedirectToDetailViewǁpost__mutmut_7, 
        'xǁRedirectToDetailViewǁpost__mutmut_8': xǁRedirectToDetailViewǁpost__mutmut_8, 
        'xǁRedirectToDetailViewǁpost__mutmut_9': xǁRedirectToDetailViewǁpost__mutmut_9, 
        'xǁRedirectToDetailViewǁpost__mutmut_10': xǁRedirectToDetailViewǁpost__mutmut_10, 
        'xǁRedirectToDetailViewǁpost__mutmut_11': xǁRedirectToDetailViewǁpost__mutmut_11, 
        'xǁRedirectToDetailViewǁpost__mutmut_12': xǁRedirectToDetailViewǁpost__mutmut_12, 
        'xǁRedirectToDetailViewǁpost__mutmut_13': xǁRedirectToDetailViewǁpost__mutmut_13, 
        'xǁRedirectToDetailViewǁpost__mutmut_14': xǁRedirectToDetailViewǁpost__mutmut_14, 
        'xǁRedirectToDetailViewǁpost__mutmut_15': xǁRedirectToDetailViewǁpost__mutmut_15, 
        'xǁRedirectToDetailViewǁpost__mutmut_16': xǁRedirectToDetailViewǁpost__mutmut_16
    }

    def post(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRedirectToDetailViewǁpost__mutmut_orig"), object.__getattribute__(self, "xǁRedirectToDetailViewǁpost__mutmut_mutants"), *args, **kwargs)
        return result 

    post.__signature__ = _mutmut_signature(xǁRedirectToDetailViewǁpost__mutmut_orig)
    xǁRedirectToDetailViewǁpost__mutmut_orig.__name__ = 'xǁRedirectToDetailViewǁpost'




        
class SimpleRecipeDetailView(View):
    def xǁSimpleRecipeDetailViewǁget__mutmut_orig(self, request):
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
    def xǁSimpleRecipeDetailViewǁget__mutmut_1(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('XXtermXX', 'No input')
        whitelist = request.GET.getlist('whitelist', ['No input'])
        blacklist = request.GET.getlist('blacklist', ['No input'])

        # Pass arguments to the context
        context = {
            'search_term': search_term,
            'whitelist': whitelist,
            'blacklist': blacklist,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_2(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('term', 'XXNo inputXX')
        whitelist = request.GET.getlist('whitelist', ['No input'])
        blacklist = request.GET.getlist('blacklist', ['No input'])

        # Pass arguments to the context
        context = {
            'search_term': search_term,
            'whitelist': whitelist,
            'blacklist': blacklist,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_3(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = None
        whitelist = request.GET.getlist('whitelist', ['No input'])
        blacklist = request.GET.getlist('blacklist', ['No input'])

        # Pass arguments to the context
        context = {
            'search_term': search_term,
            'whitelist': whitelist,
            'blacklist': blacklist,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_4(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('term', 'No input')
        whitelist = request.GET.getlist('XXwhitelistXX', ['No input'])
        blacklist = request.GET.getlist('blacklist', ['No input'])

        # Pass arguments to the context
        context = {
            'search_term': search_term,
            'whitelist': whitelist,
            'blacklist': blacklist,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_5(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('term', 'No input')
        whitelist = request.GET.getlist('whitelist', ['XXNo inputXX'])
        blacklist = request.GET.getlist('blacklist', ['No input'])

        # Pass arguments to the context
        context = {
            'search_term': search_term,
            'whitelist': whitelist,
            'blacklist': blacklist,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_6(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('term', 'No input')
        whitelist = None
        blacklist = request.GET.getlist('blacklist', ['No input'])

        # Pass arguments to the context
        context = {
            'search_term': search_term,
            'whitelist': whitelist,
            'blacklist': blacklist,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_7(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('term', 'No input')
        whitelist = request.GET.getlist('whitelist', ['No input'])
        blacklist = request.GET.getlist('XXblacklistXX', ['No input'])

        # Pass arguments to the context
        context = {
            'search_term': search_term,
            'whitelist': whitelist,
            'blacklist': blacklist,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_8(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('term', 'No input')
        whitelist = request.GET.getlist('whitelist', ['No input'])
        blacklist = request.GET.getlist('blacklist', ['XXNo inputXX'])

        # Pass arguments to the context
        context = {
            'search_term': search_term,
            'whitelist': whitelist,
            'blacklist': blacklist,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_9(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('term', 'No input')
        whitelist = request.GET.getlist('whitelist', ['No input'])
        blacklist = None

        # Pass arguments to the context
        context = {
            'search_term': search_term,
            'whitelist': whitelist,
            'blacklist': blacklist,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_10(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('term', 'No input')
        whitelist = request.GET.getlist('whitelist', ['No input'])
        blacklist = request.GET.getlist('blacklist', ['No input'])

        # Pass arguments to the context
        context = {
            'XXsearch_termXX': search_term,
            'whitelist': whitelist,
            'blacklist': blacklist,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_11(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('term', 'No input')
        whitelist = request.GET.getlist('whitelist', ['No input'])
        blacklist = request.GET.getlist('blacklist', ['No input'])

        # Pass arguments to the context
        context = {
            'search_term': search_term,
            'XXwhitelistXX': whitelist,
            'blacklist': blacklist,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_12(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('term', 'No input')
        whitelist = request.GET.getlist('whitelist', ['No input'])
        blacklist = request.GET.getlist('blacklist', ['No input'])

        # Pass arguments to the context
        context = {
            'search_term': search_term,
            'whitelist': whitelist,
            'XXblacklistXX': blacklist,
        }
        return render(request, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_13(self, request):
        # Retrieve arguments from GET parameters or set default values
        search_term = request.GET.get('term', 'No input')
        whitelist = request.GET.getlist('whitelist', ['No input'])
        blacklist = request.GET.getlist('blacklist', ['No input'])

        # Pass arguments to the context
        context = None
        return render(request, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_14(self, request):
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
        return render(None, 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_15(self, request):
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
        return render(request, 'XXcookapp/simple_recipe_detail.htmlXX', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_16(self, request):
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
        return render(request, 'cookapp/simple_recipe_detail.html', None)
    def xǁSimpleRecipeDetailViewǁget__mutmut_17(self, request):
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
        return render( 'cookapp/simple_recipe_detail.html', context)
    def xǁSimpleRecipeDetailViewǁget__mutmut_18(self, request):
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
        return render(request, 'cookapp/simple_recipe_detail.html',)

    xǁSimpleRecipeDetailViewǁget__mutmut_mutants = {
    'xǁSimpleRecipeDetailViewǁget__mutmut_1': xǁSimpleRecipeDetailViewǁget__mutmut_1, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_2': xǁSimpleRecipeDetailViewǁget__mutmut_2, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_3': xǁSimpleRecipeDetailViewǁget__mutmut_3, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_4': xǁSimpleRecipeDetailViewǁget__mutmut_4, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_5': xǁSimpleRecipeDetailViewǁget__mutmut_5, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_6': xǁSimpleRecipeDetailViewǁget__mutmut_6, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_7': xǁSimpleRecipeDetailViewǁget__mutmut_7, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_8': xǁSimpleRecipeDetailViewǁget__mutmut_8, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_9': xǁSimpleRecipeDetailViewǁget__mutmut_9, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_10': xǁSimpleRecipeDetailViewǁget__mutmut_10, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_11': xǁSimpleRecipeDetailViewǁget__mutmut_11, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_12': xǁSimpleRecipeDetailViewǁget__mutmut_12, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_13': xǁSimpleRecipeDetailViewǁget__mutmut_13, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_14': xǁSimpleRecipeDetailViewǁget__mutmut_14, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_15': xǁSimpleRecipeDetailViewǁget__mutmut_15, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_16': xǁSimpleRecipeDetailViewǁget__mutmut_16, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_17': xǁSimpleRecipeDetailViewǁget__mutmut_17, 
        'xǁSimpleRecipeDetailViewǁget__mutmut_18': xǁSimpleRecipeDetailViewǁget__mutmut_18
    }

    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSimpleRecipeDetailViewǁget__mutmut_orig"), object.__getattribute__(self, "xǁSimpleRecipeDetailViewǁget__mutmut_mutants"), *args, **kwargs)
        return result 

    get.__signature__ = _mutmut_signature(xǁSimpleRecipeDetailViewǁget__mutmut_orig)
    xǁSimpleRecipeDetailViewǁget__mutmut_orig.__name__ = 'xǁSimpleRecipeDetailViewǁget'



class RecipeListView(ListView):
    model = Recipe
    template_name = 'cookapp/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 12

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_orig(self):
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_1(self):
        queryset = None
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_2(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('XXsortXX', 'name')  # Default to 'name' for A-Z sorting

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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_3(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'XXnameXX')  # Default to 'name' for A-Z sorting

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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_4(self):
        queryset = super().get_queryset()
        sort = None  # Default to 'name' for A-Z sorting

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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_5(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort != 'name_desc':
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_6(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'XXname_descXX':
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_7(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('XX-titleXX')
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_8(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = None
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_9(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort != 'rating':
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_10(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'XXratingXX':
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_11(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=1, then=Value(None)),
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_12(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When( then=Value(None)),
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_13(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=0,),
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_14(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=0, then=Value(None)),
                    default='XXaverage_ratingXX',
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_15(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=0, then=Value(None)),
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_16(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = queryset.annotate(
                rating_case=Case(
                    When(average_rating=0, then=Value(None)),
                    default='average_rating',
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_17(self):
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
            ).order_by('XX-rating_caseXX', '-average_rating', 'title')  # First by non-zero ratings, then by rating
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_18(self):
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
            ).order_by('-rating_case', 'XX-average_ratingXX', 'title')  # First by non-zero ratings, then by rating
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_19(self):
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
            ).order_by('-rating_case', '-average_rating', 'XXtitleXX')  # First by non-zero ratings, then by rating
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_20(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'name')  # Default to 'name' for A-Z sorting

        if sort == 'name_desc':
            queryset = queryset.order_by('-title')
        elif sort == 'rating':
            queryset = None  # First by non-zero ratings, then by rating
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_21(self):
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
        elif sort != 'rating_asc':
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_22(self):
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
        elif sort == 'XXrating_ascXX':
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

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_23(self):
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
                    When(average_rating=1, then=Value(None)),
                    default='average_rating',
                    output_field=IntegerField(),
                )
            ).order_by('rating_case', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_24(self):
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
                    When( then=Value(None)),
                    default='average_rating',
                    output_field=IntegerField(),
                )
            ).order_by('rating_case', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_25(self):
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
                    When(average_rating=0,),
                    default='average_rating',
                    output_field=IntegerField(),
                )
            ).order_by('rating_case', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_26(self):
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
                    default='XXaverage_ratingXX',
                    output_field=IntegerField(),
                )
            ).order_by('rating_case', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_27(self):
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
                    output_field=IntegerField(),
                )
            ).order_by('rating_case', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_28(self):
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
                )
            ).order_by('rating_case', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_29(self):
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
            ).order_by('XXrating_caseXX', 'average_rating', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_30(self):
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
            ).order_by('rating_case', 'XXaverage_ratingXX', 'title')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_31(self):
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
            ).order_by('rating_case', 'average_rating', 'XXtitleXX')  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_32(self):
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
            queryset = None  # First by non-zero ratings, then by rating
        else:
            queryset = queryset.order_by('title')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_33(self):
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
            queryset = queryset.order_by('XXtitleXX')

        return queryset

    # Query for recipes depending on filter dropdown
    def xǁRecipeListViewǁget_queryset__mutmut_34(self):
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
            queryset = None

        return queryset

    xǁRecipeListViewǁget_queryset__mutmut_mutants = {
    'xǁRecipeListViewǁget_queryset__mutmut_1': xǁRecipeListViewǁget_queryset__mutmut_1, 
        'xǁRecipeListViewǁget_queryset__mutmut_2': xǁRecipeListViewǁget_queryset__mutmut_2, 
        'xǁRecipeListViewǁget_queryset__mutmut_3': xǁRecipeListViewǁget_queryset__mutmut_3, 
        'xǁRecipeListViewǁget_queryset__mutmut_4': xǁRecipeListViewǁget_queryset__mutmut_4, 
        'xǁRecipeListViewǁget_queryset__mutmut_5': xǁRecipeListViewǁget_queryset__mutmut_5, 
        'xǁRecipeListViewǁget_queryset__mutmut_6': xǁRecipeListViewǁget_queryset__mutmut_6, 
        'xǁRecipeListViewǁget_queryset__mutmut_7': xǁRecipeListViewǁget_queryset__mutmut_7, 
        'xǁRecipeListViewǁget_queryset__mutmut_8': xǁRecipeListViewǁget_queryset__mutmut_8, 
        'xǁRecipeListViewǁget_queryset__mutmut_9': xǁRecipeListViewǁget_queryset__mutmut_9, 
        'xǁRecipeListViewǁget_queryset__mutmut_10': xǁRecipeListViewǁget_queryset__mutmut_10, 
        'xǁRecipeListViewǁget_queryset__mutmut_11': xǁRecipeListViewǁget_queryset__mutmut_11, 
        'xǁRecipeListViewǁget_queryset__mutmut_12': xǁRecipeListViewǁget_queryset__mutmut_12, 
        'xǁRecipeListViewǁget_queryset__mutmut_13': xǁRecipeListViewǁget_queryset__mutmut_13, 
        'xǁRecipeListViewǁget_queryset__mutmut_14': xǁRecipeListViewǁget_queryset__mutmut_14, 
        'xǁRecipeListViewǁget_queryset__mutmut_15': xǁRecipeListViewǁget_queryset__mutmut_15, 
        'xǁRecipeListViewǁget_queryset__mutmut_16': xǁRecipeListViewǁget_queryset__mutmut_16, 
        'xǁRecipeListViewǁget_queryset__mutmut_17': xǁRecipeListViewǁget_queryset__mutmut_17, 
        'xǁRecipeListViewǁget_queryset__mutmut_18': xǁRecipeListViewǁget_queryset__mutmut_18, 
        'xǁRecipeListViewǁget_queryset__mutmut_19': xǁRecipeListViewǁget_queryset__mutmut_19, 
        'xǁRecipeListViewǁget_queryset__mutmut_20': xǁRecipeListViewǁget_queryset__mutmut_20, 
        'xǁRecipeListViewǁget_queryset__mutmut_21': xǁRecipeListViewǁget_queryset__mutmut_21, 
        'xǁRecipeListViewǁget_queryset__mutmut_22': xǁRecipeListViewǁget_queryset__mutmut_22, 
        'xǁRecipeListViewǁget_queryset__mutmut_23': xǁRecipeListViewǁget_queryset__mutmut_23, 
        'xǁRecipeListViewǁget_queryset__mutmut_24': xǁRecipeListViewǁget_queryset__mutmut_24, 
        'xǁRecipeListViewǁget_queryset__mutmut_25': xǁRecipeListViewǁget_queryset__mutmut_25, 
        'xǁRecipeListViewǁget_queryset__mutmut_26': xǁRecipeListViewǁget_queryset__mutmut_26, 
        'xǁRecipeListViewǁget_queryset__mutmut_27': xǁRecipeListViewǁget_queryset__mutmut_27, 
        'xǁRecipeListViewǁget_queryset__mutmut_28': xǁRecipeListViewǁget_queryset__mutmut_28, 
        'xǁRecipeListViewǁget_queryset__mutmut_29': xǁRecipeListViewǁget_queryset__mutmut_29, 
        'xǁRecipeListViewǁget_queryset__mutmut_30': xǁRecipeListViewǁget_queryset__mutmut_30, 
        'xǁRecipeListViewǁget_queryset__mutmut_31': xǁRecipeListViewǁget_queryset__mutmut_31, 
        'xǁRecipeListViewǁget_queryset__mutmut_32': xǁRecipeListViewǁget_queryset__mutmut_32, 
        'xǁRecipeListViewǁget_queryset__mutmut_33': xǁRecipeListViewǁget_queryset__mutmut_33, 
        'xǁRecipeListViewǁget_queryset__mutmut_34': xǁRecipeListViewǁget_queryset__mutmut_34
    }

    def get_queryset(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeListViewǁget_queryset__mutmut_orig"), object.__getattribute__(self, "xǁRecipeListViewǁget_queryset__mutmut_mutants"), *args, **kwargs)
        return result 

    get_queryset.__signature__ = _mutmut_signature(xǁRecipeListViewǁget_queryset__mutmut_orig)
    xǁRecipeListViewǁget_queryset__mutmut_orig.__name__ = 'xǁRecipeListViewǁget_queryset'



def x_create_recipe__mutmut_orig(request):
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

def x_create_recipe__mutmut_1(request):
    if request.method != 'POST':
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

def x_create_recipe__mutmut_2(request):
    if request.method == 'XXPOSTXX':
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

def x_create_recipe__mutmut_3(request):
    if request.method == 'POST':
        form = None
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

def x_create_recipe__mutmut_4(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=True)
            
            # If the recipe doesn't have an API ID, generate one
            if not recipe.api_id:
                recipe.api_id = str(uuid.uuid4())
                
            recipe.save()

            return redirect('add_ingredients', recipe_id=recipe.id)
    else:
        form = RecipeForm()

    return render(request, 'cookapp/create_recipe.html', {'form': form})

def x_create_recipe__mutmut_5(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = None
            
            # If the recipe doesn't have an API ID, generate one
            if not recipe.api_id:
                recipe.api_id = str(uuid.uuid4())
                
            recipe.save()

            return redirect('add_ingredients', recipe_id=recipe.id)
    else:
        form = RecipeForm()

    return render(request, 'cookapp/create_recipe.html', {'form': form})

def x_create_recipe__mutmut_6(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            
            # If the recipe doesn't have an API ID, generate one
            if  recipe.api_id:
                recipe.api_id = str(uuid.uuid4())
                
            recipe.save()

            return redirect('add_ingredients', recipe_id=recipe.id)
    else:
        form = RecipeForm()

    return render(request, 'cookapp/create_recipe.html', {'form': form})

def x_create_recipe__mutmut_7(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            
            # If the recipe doesn't have an API ID, generate one
            if not recipe.api_id:
                recipe.api_id = None
                
            recipe.save()

            return redirect('add_ingredients', recipe_id=recipe.id)
    else:
        form = RecipeForm()

    return render(request, 'cookapp/create_recipe.html', {'form': form})

def x_create_recipe__mutmut_8(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            
            # If the recipe doesn't have an API ID, generate one
            if not recipe.api_id:
                recipe.api_id = str(uuid.uuid4())
                
            recipe.save()

            return redirect('XXadd_ingredientsXX', recipe_id=recipe.id)
    else:
        form = RecipeForm()

    return render(request, 'cookapp/create_recipe.html', {'form': form})

def x_create_recipe__mutmut_9(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            
            # If the recipe doesn't have an API ID, generate one
            if not recipe.api_id:
                recipe.api_id = str(uuid.uuid4())
                
            recipe.save()

            return redirect('add_ingredients',)
    else:
        form = RecipeForm()

    return render(request, 'cookapp/create_recipe.html', {'form': form})

def x_create_recipe__mutmut_10(request):
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
        form = None

    return render(request, 'cookapp/create_recipe.html', {'form': form})

def x_create_recipe__mutmut_11(request):
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

    return render(None, 'cookapp/create_recipe.html', {'form': form})

def x_create_recipe__mutmut_12(request):
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

    return render(request, 'XXcookapp/create_recipe.htmlXX', {'form': form})

def x_create_recipe__mutmut_13(request):
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

    return render(request, 'cookapp/create_recipe.html', {'XXformXX': form})

def x_create_recipe__mutmut_14(request):
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

    return render( 'cookapp/create_recipe.html', {'form': form})

x_create_recipe__mutmut_mutants = {
'x_create_recipe__mutmut_1': x_create_recipe__mutmut_1, 
    'x_create_recipe__mutmut_2': x_create_recipe__mutmut_2, 
    'x_create_recipe__mutmut_3': x_create_recipe__mutmut_3, 
    'x_create_recipe__mutmut_4': x_create_recipe__mutmut_4, 
    'x_create_recipe__mutmut_5': x_create_recipe__mutmut_5, 
    'x_create_recipe__mutmut_6': x_create_recipe__mutmut_6, 
    'x_create_recipe__mutmut_7': x_create_recipe__mutmut_7, 
    'x_create_recipe__mutmut_8': x_create_recipe__mutmut_8, 
    'x_create_recipe__mutmut_9': x_create_recipe__mutmut_9, 
    'x_create_recipe__mutmut_10': x_create_recipe__mutmut_10, 
    'x_create_recipe__mutmut_11': x_create_recipe__mutmut_11, 
    'x_create_recipe__mutmut_12': x_create_recipe__mutmut_12, 
    'x_create_recipe__mutmut_13': x_create_recipe__mutmut_13, 
    'x_create_recipe__mutmut_14': x_create_recipe__mutmut_14
}

def create_recipe(*args, **kwargs):
    result = _mutmut_trampoline(x_create_recipe__mutmut_orig, x_create_recipe__mutmut_mutants, *args, **kwargs)
    return result 

create_recipe.__signature__ = _mutmut_signature(x_create_recipe__mutmut_orig)
x_create_recipe__mutmut_orig.__name__ = 'x_create_recipe'




# Define the formset for RecipeIngredient in the views
RecipeIngredientFormSet = modelformset_factory(
    RecipeIngredient,
    form=RecipeIngredientForm,
    extra=5,  # Allows up to 5 ingredients to be added
)

def x_add_ingredients__mutmut_orig(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_1(request, recipe_id):
    recipe = get_object_or_404(None, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_2(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=None)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_3(request, recipe_id):
    recipe = get_object_or_404( id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_4(request, recipe_id):
    recipe = get_object_or_404(Recipe,)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_5(request, recipe_id):
    recipe = None

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_6(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method != 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_7(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'XXPOSTXX':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_8(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST,)
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_9(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = None
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_10(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=True)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_11(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = None
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_12(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = None
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_13(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('XXindexXX')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_14(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = None

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_15(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(None, 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_16(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'XXcookapp/add_ingredients.htmlXX', {'formset': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_17(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'XXformsetXX': formset, 'recipe': recipe})

def x_add_ingredients__mutmut_18(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render(request, 'cookapp/add_ingredients.html', {'formset': formset, 'XXrecipeXX': recipe})

def x_add_ingredients__mutmut_19(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        formset = RecipeIngredientFormSet(request.POST, queryset=RecipeIngredient.objects.none())
        if formset.is_valid():
            # Save the valid forms with data
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()
            # Redirect after saving
            return redirect('index')
    else:
        formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())

    return render( 'cookapp/add_ingredients.html', {'formset': formset, 'recipe': recipe})

x_add_ingredients__mutmut_mutants = {
'x_add_ingredients__mutmut_1': x_add_ingredients__mutmut_1, 
    'x_add_ingredients__mutmut_2': x_add_ingredients__mutmut_2, 
    'x_add_ingredients__mutmut_3': x_add_ingredients__mutmut_3, 
    'x_add_ingredients__mutmut_4': x_add_ingredients__mutmut_4, 
    'x_add_ingredients__mutmut_5': x_add_ingredients__mutmut_5, 
    'x_add_ingredients__mutmut_6': x_add_ingredients__mutmut_6, 
    'x_add_ingredients__mutmut_7': x_add_ingredients__mutmut_7, 
    'x_add_ingredients__mutmut_8': x_add_ingredients__mutmut_8, 
    'x_add_ingredients__mutmut_9': x_add_ingredients__mutmut_9, 
    'x_add_ingredients__mutmut_10': x_add_ingredients__mutmut_10, 
    'x_add_ingredients__mutmut_11': x_add_ingredients__mutmut_11, 
    'x_add_ingredients__mutmut_12': x_add_ingredients__mutmut_12, 
    'x_add_ingredients__mutmut_13': x_add_ingredients__mutmut_13, 
    'x_add_ingredients__mutmut_14': x_add_ingredients__mutmut_14, 
    'x_add_ingredients__mutmut_15': x_add_ingredients__mutmut_15, 
    'x_add_ingredients__mutmut_16': x_add_ingredients__mutmut_16, 
    'x_add_ingredients__mutmut_17': x_add_ingredients__mutmut_17, 
    'x_add_ingredients__mutmut_18': x_add_ingredients__mutmut_18, 
    'x_add_ingredients__mutmut_19': x_add_ingredients__mutmut_19
}

def add_ingredients(*args, **kwargs):
    result = _mutmut_trampoline(x_add_ingredients__mutmut_orig, x_add_ingredients__mutmut_mutants, *args, **kwargs)
    return result 

add_ingredients.__signature__ = _mutmut_signature(x_add_ingredients__mutmut_orig)
x_add_ingredients__mutmut_orig.__name__ = 'x_add_ingredients'


