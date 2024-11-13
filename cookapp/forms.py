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

    def clean_tags(self):
        tags = self.cleaned_data['tags']
        if isinstance(tags, str):
            return [tag.strip() for tag in tags.split(',')]
        elif isinstance(tags, list):
            return [tag.strip() for tag in tags]
        return []

    def clean_macros(self):
        # Exclude calories from macros
        return {
            'protein': self.cleaned_data.get('protein', 0),
            'carbs': self.cleaned_data.get('carbs', 0),
            'fat': self.cleaned_data.get('fat', 0),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.macros = self.clean_macros()
        instance.tags = self.clean_tags()
        
        if commit:
            instance.save()
        return instance
