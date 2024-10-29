import os
import sys
import django
import requests
import json
from openai import OpenAI

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)).rsplit('/', 3)[0])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "needtocook.settings")
django.setup()

# Now import Django models
from cookapp.models import Recipe, Ingredient, RecipeIngredient

# Initialize OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Fetch a single recipe
recipe_name = 'Arrabiata'  # Change to the recipe you want to test
url = f'https://www.themealdb.com/api/json/v1/1/search.php?s={recipe_name}'
response = requests.get(url)

if response.status_code != 200:
    print('Failed to fetch data')
elif not response.json().get('meals'):
    print('No meals found')
else:
    meal_data = response.json()['meals'][0]

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
            ingredients.append((normalized_name, quantity.strip() if quantity else None))

    # Prepare data for LLM
    basic_recipe_data = {
        'title': title,
        'ingredients': [f"{qty} {ing}".strip() for ing, qty in ingredients],
        'instructions': instructions,
    }

    # Construct the prompt
    prompt = f"""
Given the following recipe details:

Title: {basic_recipe_data['title']}

Ingredients:
{', '.join(basic_recipe_data['ingredients'])}

Instructions:
{basic_recipe_data['instructions']}

Please perform the following tasks:

1. Normalize the ingredient names (e.g., singular form, consistent naming).
2. Clean up and format the instructions with numbered steps.
3. Generate relevant tags for the recipe (e.g., vegan, gluten-free).
4. Estimate the total calories and macros (proteins, carbs, fats) if not provided.
5. Include the quantities for each ingredient.

Provide the output in JSON format with the following structure (no additional text):
Ensure all naming conventions are consistent (Capitalize appropriately)
{{
    "title": "Recipe Title",
    "ingredients": [
        {{"name": "ingredient1", "quantity": "quantity1"}},
        {{"name": "ingredient2", "quantity": "quantity2"}}
    ],
    "instructions": "Formatted instructions",
    "tags": ["tag1", "tag2", ...],
    "calories": total_calories,
    "macros": {{
        "proteins": grams_protein,
        "carbs": grams_carbs,
        "fats": grams_fat
    }}
}}
"""

    # Call the OpenAI API using the new method
    try:
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )

        output_text = response.choices[0].message.content.strip()
        # Remove any backticks that might be present
        output_text = output_text.replace("```json", "").replace("```", "").strip()

        print("LLM Output:")
        print(output_text)

        # Parse the JSON output
        try:
            enhanced_data = json.loads(output_text)
            print("\nParsed Enhanced Data:")
            print(json.dumps(enhanced_data, indent=4))

            # Create or update the recipe in the database using the enhanced data
            title = enhanced_data.get('title', 'Unknown Recipe')
            instructions = enhanced_data.get('instructions', '')
            tags = enhanced_data.get('tags', [])
            calories = enhanced_data.get('calories', None)
            macros = enhanced_data.get('macros', {})
            ingredient_details = enhanced_data.get('ingredients', [])

            # Create or update Recipe
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

            # Create or get Ingredient instances and add to recipe through RecipeIngredient
            for item in ingredient_details:
                name = item['name'].strip().lower()
                quantity = item.get('quantity', '')
                ingredient, _ = Ingredient.objects.get_or_create(name=name)

                # Create RecipeIngredient link
                RecipeIngredient.objects.update_or_create(
                    recipe=recipe,
                    ingredient=ingredient,
                    defaults={'quantity': quantity}
                )

            # Print the details of the created recipe
            print("\nCreated Recipe Details:")
            print(f"Title: {recipe.title}")
            print(f"Ingredients: {[f'{ri.ingredient.name} ({ri.quantity})' for ri in RecipeIngredient.objects.filter(recipe=recipe)]}")
            print(f"Instructions: {recipe.instructions}")
            print(f"Calories: {recipe.calories}")
            print(f"Macros: {recipe.macros}")
            print(f"Tags: {recipe.tags}")

        except json.JSONDecodeError as e:
            print(f'JSON decoding error: {e}')
            print('Raw LLM output:')
            print(output_text)

    except Exception as e:
        print(f'Error calling LLM: {e}')
