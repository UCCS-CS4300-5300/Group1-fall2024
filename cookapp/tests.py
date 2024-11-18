from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from cookapp.models import Ingredient, Recipe, UserPreference, Diets, RecipeIngredient, Rating

class UserTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            username="test_user",
            email="test@user.com",
            password="test1234",
        )

    def test_user_created(self):
        self.assertEqual(self.test_user.username, "test_user")
        self.assertEqual(self.test_user.password, "test1234")
        self.assertEqual(self.test_user.email, "test@user.com")

class IndexTestCase(TestCase):
    def test_index_view(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookapp/index.html')

# Integration tests for Blacklist
class RecipeSearchIntegrationTests(TestCase):
    def setUp(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(
            title='Tomato Soup',
            api_id='api_001',
            instructions='Boil the tomatoes.',
            calories=150,
        )
        RecipeIngredient.objects.create(recipe=self.recipe1, ingredient=self.ingredient1, quantity="2 cups")

        self.recipe2 = Recipe.objects.create(
            title='Onion Soup',
            api_id='api_002',
            instructions='Cook onions.',
            calories=100,
        )
        RecipeIngredient.objects.create(recipe=self.recipe2, ingredient=self.ingredient2, quantity="1 cup")

        self.recipe3 = Recipe.objects.create(
            title='Garlic Bread',
            api_id='api_003',
            instructions='Bake garlic in bread.',
            calories=200,
        )
        RecipeIngredient.objects.create(recipe=self.recipe3, ingredient=self.ingredient3, quantity="3 cloves")

        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_blacklisted_ingredients_exclusion(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def test_blacklisted_ingredients_no_results(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

# Unit tests for Blacklist
class RecipeSearchUnitTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', api_id='api_001', calories=150)
        RecipeIngredient.objects.create(recipe=self.recipe1, ingredient=self.ingredient1, quantity="2 cups")

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='api_002', calories=100)
        RecipeIngredient.objects.create(recipe=self.recipe2, ingredient=self.ingredient2, quantity="1 cup")

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        RecipeIngredient.objects.create(recipe=self.recipe3, ingredient=self.ingredient3, quantity="3 cloves")

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def test_add_to_blacklist(self):
        # Add ingredient to blacklist
        self.user_pref.blacklist.add(self.ingredient1)
        self.assertIn(self.ingredient1, self.user_pref.blacklist.all())

    def test_remove_from_blacklist(self):
        # Add and remove an ingredient from the blacklist
        self.user_pref.blacklist.add(self.ingredient1)
        self.user_pref.blacklist.remove(self.ingredient1)
        self.assertNotIn(self.ingredient1, self.user_pref.blacklist.all())

    def test_multiple_ingredients_in_blacklist(self):
        # Add multiple ingredients to the blacklist
        self.user_pref.blacklist.add(self.ingredient1, self.ingredient2)
        self.assertIn(self.ingredient1, self.user_pref.blacklist.all())
        self.assertIn(self.ingredient2, self.user_pref.blacklist.all())

    def test_blacklist_filtering(self):
        # Test filtering recipes based on blacklist
        blacklist = ['Onion']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(recipeingredient__ingredient__name__in=blacklist)

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2, filtered_recipes)
        self.assertIn(self.recipe1, filtered_recipes)
        self.assertIn(self.recipe3, filtered_recipes)

    def test_blacklist_with_no_results(self):
        # Test with blacklist that excludes all recipes
        blacklist = ['Onion', 'Tomato', 'Garlic']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(recipeingredient__ingredient__name__in=blacklist)

        # Check that no recipes are returned
        self.assertEqual(filtered_recipes.count(), 0)

class AllergenFunctionTests(TestCase):
    def setUp(self):
        # Create ingredients
        self.peanut = Ingredient.objects.create(name="Peanut")
        self.flour = Ingredient.objects.create(name="Flour")
        self.sugar = Ingredient.objects.create(name="Sugar")

        # Create dietary restriction
        self.allergy = Diets.objects.create(name="Nut Allergy")
        self.allergy.blacklist.add(self.peanut)

        # Create a recipe
        self.recipe = Recipe.objects.create(
            title="Peanut Butter Cookies",
            api_id="12345",
            instructions="Mix ingredients and bake.",
        )

        # Link ingredients to recipe
        RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.peanut, quantity="100g")
        RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.flour, quantity="200g")
        RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.sugar, quantity="150g")

        # Create user and preferences
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.user_preference = UserPreference.objects.create(user=self.user)
        self.user_preference.blacklist.add(self.peanut)

    def test_recipe_ingredients_respects_blacklist(self):
        """Test that a recipe is correctly identified as containing blacklisted ingredients."""
        recipe_ingredients = RecipeIngredient.objects.filter(recipe=self.recipe)
        ingredient_ids = [ri.ingredient.id for ri in recipe_ingredients]
        blacklist_ids = self.user_preference.blacklist.values_list('id', flat=True)

        contains_blacklisted = any(ingredient in blacklist_ids for ingredient in ingredient_ids)
        self.assertTrue(contains_blacklisted)

    def test_recipe_without_blacklisted_ingredients(self):
        """Test that a recipe without blacklisted ingredients passes the filter."""
        self.user_preference.blacklist.clear()  # Clear blacklist to simulate no restriction
        blacklist_ids = self.user_preference.blacklist.values_list('id', flat=True)

        recipe_ingredients = RecipeIngredient.objects.filter(recipe=self.recipe)
        ingredient_ids = [ri.ingredient.id for ri in recipe_ingredients]

        contains_blacklisted = any(ingredient in blacklist_ids for ingredient in ingredient_ids)
        self.assertFalse(contains_blacklisted)


class IngredientModelTest(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(name="Tomato", tags=["vegetarian", "gluten-free"])

    def test_ingredient_creation(self):
        self.assertEqual(self.ingredient.name, "Tomato")
        self.assertEqual(self.ingredient.tags, ["vegetarian", "gluten-free"])
        self.assertEqual(str(self.ingredient), "Tomato")

    def test_ingredient_ordering(self):
        ingredient2 = Ingredient.objects.create(name="Apple")
        ingredients = Ingredient.objects.all()
        self.assertEqual(ingredients[0].name, "Apple")
        self.assertEqual(ingredients[1].name, "Tomato")

class RecipeModelTest(TestCase):
    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(name="Tomato")
        self.ingredient2 = Ingredient.objects.create(name="Cheese")
        
        self.recipe = Recipe.objects.create(
            title="Tomato Cheese Salad",
            api_id="12345",
            instructions="Mix tomatoes and cheese.",
            calories=200,
            macros={"protein": 10, "carbs": 15, "fat": 10},
            tags=["quick", "easy"]
        )
        
        RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.ingredient1, quantity="2 cups")
        RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.ingredient2, quantity="1 cup")

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, "Tomato Cheese Salad")
        self.assertEqual(self.recipe.api_id, "12345")
        self.assertEqual(self.recipe.instructions, "Mix tomatoes and cheese.")
        self.assertEqual(self.recipe.calories, 200)
        self.assertEqual(self.recipe.macros, {"protein": 10, "carbs": 15, "fat": 10})
        self.assertEqual(self.recipe.tags, ["quick", "easy"])
        self.assertEqual(str(self.recipe), "Tomato Cheese Salad")
        self.assertIn(self.ingredient1, [ri.ingredient for ri in self.recipe.recipeingredient_set.all()])
        self.assertIn(self.ingredient2, [ri.ingredient for ri in self.recipe.recipeingredient_set.all()])

    def test_recipe_ordering(self):
        recipe2 = Recipe.objects.create(title="Apple Pie", api_id="67890")
        recipes = Recipe.objects.all()
        self.assertEqual(recipes[0].title, "Apple Pie")
        self.assertEqual(recipes[1].title, "Tomato Cheese Salad")

class UserPreferenceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.ingredient1 = Ingredient.objects.create(name="Tomato")
        self.ingredient2 = Ingredient.objects.create(name="Cheese")
        self.user_preference = UserPreference.objects.create(user=self.user)
        self.user_preference.whitelist.add(self.ingredient1)
        self.user_preference.blacklist.add(self.ingredient2)

    def test_user_preference_creation(self):
        self.assertEqual(self.user_preference.user.username, "testuser")
        self.assertIn(self.ingredient1, self.user_preference.whitelist.all())
        self.assertIn(self.ingredient2, self.user_preference.blacklist.all())
        self.assertEqual(str(self.user_preference), "testuser's preferences")

class RatingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.recipe = Recipe.objects.create(
            title="Tomato Cheese Salad",
            api_id="12345",
            instructions="Mix tomatoes and cheese.",
            calories=200,
            macros={"protein": 10, "carbs": 15, "fat": 10},
            tags=["quick", "easy"]
        )
        self.rating = Rating.objects.create(user=self.user, recipe=self.recipe, value=5, review="Delicious!")

    def test_rating_creation(self):
        self.assertEqual(self.rating.user.username, "testuser")
        self.assertEqual(self.rating.recipe.title, "Tomato Cheese Salad")
        self.assertEqual(self.rating.value, 5)
        self.assertEqual(self.rating.review, "Delicious!")
        self.assertEqual(str(self.rating), "testuser rated Tomato Cheese Salad as 5")

    def test_update_average_rating(self):
        self.recipe.update_average_rating()
        self.assertEqual(self.recipe.average_rating, 5.0)

class MealPlanViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_meal_plan_view(self):
        response = self.client.get(reverse('meal_plan'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookapp/mealPlanner.html')
        self.assertContains(response, 'Weekly Meal Planner')

    def test_save_meal_plan(self):
        meal_plan = {
            "Monday": {
                "Breakfast": "<div class='card meal-card'>Recipe 1</div>",
                "Lunch": "<div class='card meal-card'>Recipe 2</div>",
                "Snack": "<div class='card meal-card'>Recipe 3</div>",
                "Dinner": "<div class='card meal-card'>Recipe 4</div>"
            }
        }
        response = self.client.post(reverse('save_meal_plan'), json.dumps(meal_plan), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'success'})

    def test_load_meal_plan(self):
        meal_plan = {
            "Monday": {
                "Breakfast": "<div class='card meal-card'>Recipe 1</div>",
                "Lunch": "<div class='card meal-card'>Recipe 2</div>",
                "Snack": "<div class='card meal-card'>Recipe 3</div>",
                "Dinner": "<div class='card meal-card'>Recipe 4</div>"
            }
        }
        self.client.post(reverse('save_meal_plan'), json.dumps(meal_plan), content_type='application/json')
        response = self.client.get(reverse('meal_plan'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Recipe 1')
        self.assertContains(response, 'Recipe 2')
        self.assertContains(response, 'Recipe 3')
        self.assertContains(response, 'Recipe 4')