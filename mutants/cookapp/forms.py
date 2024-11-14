
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


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Recipe, Ingredient, RecipeIngredient
from django.forms import modelformset_factory

# Define forms for user creation, recipe, and recipe ingredients
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']  # Replace with actual fields in the RecipeIngredient model
class RecipeForm(forms.ModelForm):
    calories = forms.IntegerField(label='Calories', required=True)
    protein = forms.IntegerField(label='Protein')
    carbs = forms.IntegerField(label='Carbohydrates')
    fat = forms.IntegerField(label='Fat')
    tags = forms.CharField(label='Tags', help_text='Enter tags separated by commas')

    class Meta:
        model = Recipe
        fields = ['title', 'instructions', 'image', 'calories', 'protein', 'carbs', 'fat', 'tags']

    def xǁRecipeFormǁclean_tags__mutmut_orig(self):
        tags = self.cleaned_data['tags']
        if isinstance(tags, str):
            return [tag.strip() for tag in tags.split(',')]
        elif isinstance(tags, list):
            return [tag.strip() for tag in tags]
        return []

    def xǁRecipeFormǁclean_tags__mutmut_1(self):
        tags = self.cleaned_data['XXtagsXX']
        if isinstance(tags, str):
            return [tag.strip() for tag in tags.split(',')]
        elif isinstance(tags, list):
            return [tag.strip() for tag in tags]
        return []

    def xǁRecipeFormǁclean_tags__mutmut_2(self):
        tags = self.cleaned_data[None]
        if isinstance(tags, str):
            return [tag.strip() for tag in tags.split(',')]
        elif isinstance(tags, list):
            return [tag.strip() for tag in tags]
        return []

    def xǁRecipeFormǁclean_tags__mutmut_3(self):
        tags = None
        if isinstance(tags, str):
            return [tag.strip() for tag in tags.split(',')]
        elif isinstance(tags, list):
            return [tag.strip() for tag in tags]
        return []

    def xǁRecipeFormǁclean_tags__mutmut_4(self):
        tags = self.cleaned_data['tags']
        if isinstance(tags, str):
            return [tag.strip() for tag in tags.split('XX,XX')]
        elif isinstance(tags, list):
            return [tag.strip() for tag in tags]
        return []

    xǁRecipeFormǁclean_tags__mutmut_mutants = {
    'xǁRecipeFormǁclean_tags__mutmut_1': xǁRecipeFormǁclean_tags__mutmut_1, 
        'xǁRecipeFormǁclean_tags__mutmut_2': xǁRecipeFormǁclean_tags__mutmut_2, 
        'xǁRecipeFormǁclean_tags__mutmut_3': xǁRecipeFormǁclean_tags__mutmut_3, 
        'xǁRecipeFormǁclean_tags__mutmut_4': xǁRecipeFormǁclean_tags__mutmut_4
    }

    def clean_tags(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeFormǁclean_tags__mutmut_orig"), object.__getattribute__(self, "xǁRecipeFormǁclean_tags__mutmut_mutants"), *args, **kwargs)
        return result 

    clean_tags.__signature__ = _mutmut_signature(xǁRecipeFormǁclean_tags__mutmut_orig)
    xǁRecipeFormǁclean_tags__mutmut_orig.__name__ = 'xǁRecipeFormǁclean_tags'



    def xǁRecipeFormǁclean_macros__mutmut_orig(self):
        # Exclude calories from macros
        return {
            'protein': self.cleaned_data.get('protein', 0),
            'carbs': self.cleaned_data.get('carbs', 0),
            'fat': self.cleaned_data.get('fat', 0),
        }

    def xǁRecipeFormǁclean_macros__mutmut_1(self):
        # Exclude calories from macros
        return {
            'XXproteinXX': self.cleaned_data.get('protein', 0),
            'carbs': self.cleaned_data.get('carbs', 0),
            'fat': self.cleaned_data.get('fat', 0),
        }

    def xǁRecipeFormǁclean_macros__mutmut_2(self):
        # Exclude calories from macros
        return {
            'protein': self.cleaned_data.get('XXproteinXX', 0),
            'carbs': self.cleaned_data.get('carbs', 0),
            'fat': self.cleaned_data.get('fat', 0),
        }

    def xǁRecipeFormǁclean_macros__mutmut_3(self):
        # Exclude calories from macros
        return {
            'protein': self.cleaned_data.get('protein', 1),
            'carbs': self.cleaned_data.get('carbs', 0),
            'fat': self.cleaned_data.get('fat', 0),
        }

    def xǁRecipeFormǁclean_macros__mutmut_4(self):
        # Exclude calories from macros
        return {
            'protein': self.cleaned_data.get('protein', 0),
            'XXcarbsXX': self.cleaned_data.get('carbs', 0),
            'fat': self.cleaned_data.get('fat', 0),
        }

    def xǁRecipeFormǁclean_macros__mutmut_5(self):
        # Exclude calories from macros
        return {
            'protein': self.cleaned_data.get('protein', 0),
            'carbs': self.cleaned_data.get('XXcarbsXX', 0),
            'fat': self.cleaned_data.get('fat', 0),
        }

    def xǁRecipeFormǁclean_macros__mutmut_6(self):
        # Exclude calories from macros
        return {
            'protein': self.cleaned_data.get('protein', 0),
            'carbs': self.cleaned_data.get('carbs', 1),
            'fat': self.cleaned_data.get('fat', 0),
        }

    def xǁRecipeFormǁclean_macros__mutmut_7(self):
        # Exclude calories from macros
        return {
            'protein': self.cleaned_data.get('protein', 0),
            'carbs': self.cleaned_data.get('carbs', 0),
            'XXfatXX': self.cleaned_data.get('fat', 0),
        }

    def xǁRecipeFormǁclean_macros__mutmut_8(self):
        # Exclude calories from macros
        return {
            'protein': self.cleaned_data.get('protein', 0),
            'carbs': self.cleaned_data.get('carbs', 0),
            'fat': self.cleaned_data.get('XXfatXX', 0),
        }

    def xǁRecipeFormǁclean_macros__mutmut_9(self):
        # Exclude calories from macros
        return {
            'protein': self.cleaned_data.get('protein', 0),
            'carbs': self.cleaned_data.get('carbs', 0),
            'fat': self.cleaned_data.get('fat', 1),
        }

    xǁRecipeFormǁclean_macros__mutmut_mutants = {
    'xǁRecipeFormǁclean_macros__mutmut_1': xǁRecipeFormǁclean_macros__mutmut_1, 
        'xǁRecipeFormǁclean_macros__mutmut_2': xǁRecipeFormǁclean_macros__mutmut_2, 
        'xǁRecipeFormǁclean_macros__mutmut_3': xǁRecipeFormǁclean_macros__mutmut_3, 
        'xǁRecipeFormǁclean_macros__mutmut_4': xǁRecipeFormǁclean_macros__mutmut_4, 
        'xǁRecipeFormǁclean_macros__mutmut_5': xǁRecipeFormǁclean_macros__mutmut_5, 
        'xǁRecipeFormǁclean_macros__mutmut_6': xǁRecipeFormǁclean_macros__mutmut_6, 
        'xǁRecipeFormǁclean_macros__mutmut_7': xǁRecipeFormǁclean_macros__mutmut_7, 
        'xǁRecipeFormǁclean_macros__mutmut_8': xǁRecipeFormǁclean_macros__mutmut_8, 
        'xǁRecipeFormǁclean_macros__mutmut_9': xǁRecipeFormǁclean_macros__mutmut_9
    }

    def clean_macros(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeFormǁclean_macros__mutmut_orig"), object.__getattribute__(self, "xǁRecipeFormǁclean_macros__mutmut_mutants"), *args, **kwargs)
        return result 

    clean_macros.__signature__ = _mutmut_signature(xǁRecipeFormǁclean_macros__mutmut_orig)
    xǁRecipeFormǁclean_macros__mutmut_orig.__name__ = 'xǁRecipeFormǁclean_macros'



    def xǁRecipeFormǁsave__mutmut_orig(self, commit=True):
        instance = super().save(commit=False)
        instance.macros = self.clean_macros()
        instance.tags = self.clean_tags()
        
        if commit:
            instance.save()
        return instance

    def xǁRecipeFormǁsave__mutmut_1(self, commit=False):
        instance = super().save(commit=False)
        instance.macros = self.clean_macros()
        instance.tags = self.clean_tags()
        
        if commit:
            instance.save()
        return instance

    def xǁRecipeFormǁsave__mutmut_2(self, commit=True):
        instance = super().save(commit=True)
        instance.macros = self.clean_macros()
        instance.tags = self.clean_tags()
        
        if commit:
            instance.save()
        return instance

    def xǁRecipeFormǁsave__mutmut_3(self, commit=True):
        instance = None
        instance.macros = self.clean_macros()
        instance.tags = self.clean_tags()
        
        if commit:
            instance.save()
        return instance

    def xǁRecipeFormǁsave__mutmut_4(self, commit=True):
        instance = super().save(commit=False)
        instance.macros = None
        instance.tags = self.clean_tags()
        
        if commit:
            instance.save()
        return instance

    def xǁRecipeFormǁsave__mutmut_5(self, commit=True):
        instance = super().save(commit=False)
        instance.macros = self.clean_macros()
        instance.tags = None
        
        if commit:
            instance.save()
        return instance

    xǁRecipeFormǁsave__mutmut_mutants = {
    'xǁRecipeFormǁsave__mutmut_1': xǁRecipeFormǁsave__mutmut_1, 
        'xǁRecipeFormǁsave__mutmut_2': xǁRecipeFormǁsave__mutmut_2, 
        'xǁRecipeFormǁsave__mutmut_3': xǁRecipeFormǁsave__mutmut_3, 
        'xǁRecipeFormǁsave__mutmut_4': xǁRecipeFormǁsave__mutmut_4, 
        'xǁRecipeFormǁsave__mutmut_5': xǁRecipeFormǁsave__mutmut_5
    }

    def save(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeFormǁsave__mutmut_orig"), object.__getattribute__(self, "xǁRecipeFormǁsave__mutmut_mutants"), *args, **kwargs)
        return result 

    save.__signature__ = _mutmut_signature(xǁRecipeFormǁsave__mutmut_orig)
    xǁRecipeFormǁsave__mutmut_orig.__name__ = 'xǁRecipeFormǁsave'


