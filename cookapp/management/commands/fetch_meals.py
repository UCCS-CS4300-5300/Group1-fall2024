# cookapp/management/commands/fetch_meals.py

import os
import json
import re
import requests
from django.core.management.base import BaseCommand
from cookapp.models import Ingredient, Recipe, RecipeIngredient
from openai import OpenAI

class Command(BaseCommand):
    help = 'Fetch all meals from TheMealDB API, enhance with LLM, and populate the database'

    def handle(self, *args, **kwargs):
        # Initialize the OpenAI client
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

        base_url = 'https://www.themealdb.com/api/json/v1/1/search.php?f='
        letters = 'abcdefghijklmnopqrstuvwxyz'  # Adjust as needed
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
                image_url = meal_data.get('strMealThumb', '').replace('\\/', '/')

                # Extract ingredients and measurements
                ingredients = []
                for i in range(1, 21):
                    ingredient_name = meal_data.get(f'strIngredient{i}')
                    quantity = meal_data.get(f'strMeasure{i}')
                    if ingredient_name and ingredient_name.strip():
                        normalized_name = ingredient_name.strip()
                        quantity = quantity.strip() if quantity else ''
                        ingredients.append((normalized_name, quantity))

                # Prepare data for LLM
                basic_recipe_data = {
                    'title': title,
                    'ingredients': ingredients,
                    'instructions': instructions,
                }

                # Enhance recipe using LLM
                enhanced_recipe_data = self.enhance_recipe_with_llm(client, basic_recipe_data)

                if enhanced_recipe_data:
                    # Create or update the recipe in the database
                    self.create_recipe_model(meal_id, enhanced_recipe_data, image_url)
                    total_meals_added += 1
                else:
                    self.stderr.write(f'Failed to enhance recipe: {title}')

        self.stdout.write(self.style.SUCCESS(f'Successfully fetched and populated {total_meals_added} recipes!'))

    def enhance_recipe_with_llm(self, client, basic_recipe_data, retries=2):
        # Construct the prompt
        prompt = f"""
Given the following recipe details:

Title: {basic_recipe_data['title']}

Ingredients:
{', '.join([f"{qty} {ing}".strip() for ing, qty in basic_recipe_data['ingredients']])}

Instructions:
{basic_recipe_data['instructions']}

Please perform the following tasks:

1. Normalize the ingredient names (e.g., singular form, consistent naming).
2. Clean up and format the instructions with numbered steps, adding newlines between each step.
3. Generate relevant tags for the recipe (e.g., vegan, gluten-free).
4. Estimate the total calories and macros (proteins, carbs, fats), if not provided.
5. Include the quantities for each ingredient.

Provide the output in JSON format with the following structure:

START_JSON
{{
    "title": "Recipe Title",
    "ingredients": [
        {{"name": "ingredient1", "quantity": "quantity1"}},
        {{"name": "ingredient2", "quantity": "quantity2"}}
    ],
    "instructions": "Formatted instructions with numbered steps and newlines",
    "tags": ["tag1", "tag2"],
    "calories": total_calories,
    "macros": {{
        "proteins": grams_protein,
        "carbs": grams_carbs,
        "fats": grams_fat
    }}
}}

Do not include any code block formatting, triple backticks, or extra text. Only output the pure JSON data.
"""

        for attempt in range(retries):
            try:
                # Use the client to call the API
                response = client.chat.completions.create(
                    model='gpt-4o-mini',
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an assistant that processes recipes and outputs data in JSON format."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=1500,
                    temperature=0.7,
                )

                output_text = response.choices[0].message.content.strip()

                # Extract JSON after 'START_JSON'
                if 'START_JSON' in output_text:
                    json_data_start = output_text.index("START_JSON") + len("START_JSON")
                    json_text = output_text[json_data_start:].strip()
                else:
                    json_text = output_text.strip()

                # Remove any code block markdown from the output
                json_text = re.sub(r'^```[a-zA-Z]*\n', '', json_text)
                json_text = re.sub(r'^```[a-zA-Z]*\r\n', '', json_text)
                json_text = re.sub(r'\n```$', '', json_text)
                json_text = re.sub(r'\r\n```$', '', json_text)

                # Attempt to parse the JSON output
                try:
                    enhanced_data = json.loads(json_text)
                    return enhanced_data
                except json.JSONDecodeError as e:
                    self.stderr.write(f'JSON decoding error for recipe \"{basic_recipe_data['title']}\": {e}')
                    self.stderr.write("Raw LLM output:")
                    self.stderr.write(output_text)
                    if attempt < retries - 1:
                        self.stderr.write(f'Attempt {attempt + 1} failed. Retrying...')
                        continue
                    else:
                        return None

            except Exception as e:
                self.stderr.write(f'Error calling LLM for recipe \"{basic_recipe_data['title']}\": {e}')
                return None

    def create_recipe_model(self, meal_id, enhanced_data, image_url):
        # Extract data
        title = enhanced_data.get('title', 'Unknown Recipe')
        instructions = enhanced_data.get('instructions', '')
        tags = enhanced_data.get('tags', [])
        calories = enhanced_data.get('calories', None)
        macros = enhanced_data.get('macros', {})
        ingredient_data = enhanced_data.get('ingredients', [])

        # Create or update the recipe
        recipe, created = Recipe.objects.update_or_create(
            api_id=meal_id,
            defaults={
                'title': title,
                'instructions': instructions,
                'image': image_url,
                'tags': tags,
                'calories': calories,
                'macros': macros,
            }
        )

        # Use a set to track processed ingredient names
        processed_ingredients = set()

        # Associate ingredients with the recipe
        for ingredient_entry in ingredient_data:
            ingredient_name = ingredient_entry.get('name')
            quantity = ingredient_entry.get('quantity', '')

            if not ingredient_name:
                continue  # Skip if ingredient name is missing

            # Normalize ingredient name
            ingredient_name_normalized = ingredient_name.strip().lower()

            # Skip if already processed
            if ingredient_name_normalized in processed_ingredients:
                continue

            processed_ingredients.add(ingredient_name_normalized)

            # Get or create the Ingredient instance
            ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_name_normalized)

            # Check if the RecipeIngredient already exists
            recipe_ingredient, created = RecipeIngredient.objects.get_or_create(
                recipe=recipe,
                ingredient=ingredient,
                defaults={'quantity': quantity}  # Set quantity only if newly created
            )

            # If it already exists and quantity needs updating, update it
            if not created and recipe_ingredient.quantity != quantity:
                recipe_ingredient.quantity = quantity
                recipe_ingredient.save()
