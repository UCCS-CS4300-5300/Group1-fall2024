# cookapp/management/commands/fetch_meals.py
import requests
from django.core.management.base import BaseCommand
from cookapp.models import Ingredient, Recipe

class Command(BaseCommand):
    help = 'Fetch all meals from TheMealDB API and populate the database'

    def handle(self, *args, **kwargs):
        base_url = 'https://www.themealdb.com/api/json/v1/1/search.php?f='
        letters = 'abcdefghijklmnopqrstuvwxyz'
        total_meals_added = 0

        for letter in letters:
            url = f'{base_url}{letter}'
            response = requests.get(url)

            if response.status_code != 200:
                self.stderr.write(f'Failed to fetch data for letter {letter}')
                continue

            meals_data = response.json().get('meals', [])
            if not meals_data:
                self.stdout.write(f'No meals found for letter {letter}')
                continue

            for meal_data in meals_data:
                # Extract meal details
                title = meal_data['strMeal']
                instructions = meal_data['strInstructions']
                meal_id = meal_data['idMeal']
                tags = meal_data.get('strTags', '').split(',') if meal_data.get('strTags') else []

                # Extract ingredients and measurements
                ingredients = []
                for i in range(1, 21):
                    ingredient_name = meal_data.get(f'strIngredient{i}')
                    if ingredient_name and ingredient_name.strip():
                        # Normalize the ingredient name to lowercase
                        normalized_name = ingredient_name.strip().lower()
                        ingredient, _ = Ingredient.objects.get_or_create(name=normalized_name)
                        ingredients.append(ingredient)

                # Create or update the recipe in the database
                recipe, created = Recipe.objects.update_or_create(
                    api_id=meal_id,
                    defaults={
                        'title': title,
                        'instructions': instructions,
                        'tags': tags,
                        'macros': {},  # TheMealDB doesn't provide nutritional info, leave empty for now
                    }
                )

                # Set the many-to-many relationship for ingredients
                recipe.ingredients.set(ingredients)
                recipe.save()

                total_meals_added += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully fetched and populated {total_meals_added} recipes!'))
