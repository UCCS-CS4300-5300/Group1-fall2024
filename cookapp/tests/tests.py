from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from cookapp.models import (
    Ingredient,
    Recipe,
    UserPreference,
    RecipeIngredient,
    FavoriteRecipe,
    Diets,
    Rating,
)


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
        RecipeIngredient.objects.create(
            recipe=self.recipe1,
            ingredient=self.ingredient1,
            quantity="2 cups",
        )

        self.recipe2 = Recipe.objects.create(
            title='Onion Soup',
            api_id='api_002',
            instructions='Cook onions.',
            calories=100,
        )
        RecipeIngredient.objects.create(
            recipe=self.recipe2,
            ingredient=self.ingredient2,
            quantity="1 cup",
        )

        self.recipe3 = Recipe.objects.create(
            title='Garlic Bread',
            api_id='api_003',
            instructions='Bake garlic in bread.',
            calories=200,
        )
        RecipeIngredient.objects.create(
            recipe=self.recipe3,
            ingredient=self.ingredient3,
            quantity="3 cloves",
        )

        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
        )

    # Blacklist Tests
    def test_blacklisted_ingredients_exclusion(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(
            reverse('recipe_search'),
            {'term': 'soup', 'blacklist': '["Onion"]'},
        )

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(
            recipes[0]['title'], 'Tomato Soup'
        )  # Tomato Soup should be in the results
        self.assertNotIn(
            'Onion Soup', [recipe['title'] for recipe in recipes]
        )  # Onion Soup should be excluded

    def test_blacklisted_ingredients_no_results(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(
            reverse('recipe_search'),
            {'term': 'soup', 'blacklist': '["Onion", "Tomato"]'},
        )

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def test_blacklisted_ingredients_only(self):
        # Simulate a GET request to the search view with only a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(
            reverse('recipe_search'),
            {'term': 'soup', 'blacklist': '["Onion"]'},
        )

        # Check that recipes containing "Onion" are excluded
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only Tomato Soup should be returned
        self.assertEqual(
            recipes[0]['title'], 'Tomato Soup'
        )  # Tomato Soup should be in the results
        self.assertNotIn(
            'Onion Soup', [recipe['title'] for recipe in recipes]
        )  # Onion Soup should be excluded

    # Whitelist Tests
    def test_whitelisted_ingredients_inclusion(self):
        # Simulate a GET request to the search view with a whitelist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(
            reverse('recipe_search'),
            {'term': 'soup', 'whitelist': '["Tomato"]'},
        )

        # Check that only Tomato Soup is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only Tomato Soup should be returned
        self.assertEqual(
            recipes[0]['title'], 'Tomato Soup'
        )  # Tomato Soup should be in the results
        self.assertNotIn(
            'Onion Soup', [recipe['title'] for recipe in recipes]
        )  # Onion Soup should not be included

    def test_whitelisted_ingredients_no_results(self):
        # Simulate a GET request to the search view with a whitelist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(
            reverse('recipe_search'),
            {'term': 'soup', 'whitelist': '["Garlic"]'},
        )

        # Check that no recipes are returned, as none contain Garlic
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def test_whitelisted_ingredients_only(self):
        # Simulate a GET request to the search view with only a whitelist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(
            reverse('recipe_search'),
            {'term': 'soup', 'whitelist': '["Tomato"]'},
        )

        # Check that only recipes containing "Tomato" are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only Tomato Soup should be returned
        self.assertEqual(
            recipes[0]['title'], 'Tomato Soup'
        )  # Tomato Soup should be in the results
        self.assertNotIn(
            'Onion Soup', [recipe['title'] for recipe in recipes]
        )  # Onion Soup should not be included


class RecipeSearchUnitTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
        )

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(
            title='Tomato Soup',
            api_id='api_001',
            calories=150,
        )
        RecipeIngredient.objects.create(
            recipe=self.recipe1,
            ingredient=self.ingredient1,
            quantity="2 cups",
        )

        self.recipe2 = Recipe.objects.create(
            title='Onion Soup',
            api_id='api_002',
            calories=100,
        )
        RecipeIngredient.objects.create(
            recipe=self.recipe2,
            ingredient=self.ingredient2,
            quantity="1 cup",
        )

        self.recipe3 = Recipe.objects.create(
            title='Garlic Bread',
            api_id='api_003',
            calories=200,
        )
        RecipeIngredient.objects.create(
            recipe=self.recipe3,
            ingredient=self.ingredient3,
            quantity="3 cloves",
        )

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    # Blacklist Tests
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
        filtered_recipes = Recipe.objects.exclude(
            recipeingredient__ingredient__name__in=blacklist
        )

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2, filtered_recipes)
        self.assertIn(self.recipe1, filtered_recipes)
        self.assertIn(self.recipe3, filtered_recipes)

    def test_blacklist_with_no_results(self):
        # Test with blacklist that excludes all recipes
        blacklist = ['Onion', 'Tomato', 'Garlic']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(
            recipeingredient__ingredient__name__in=blacklist
        )

        # Check that no recipes are returned
        self.assertEqual(filtered_recipes.count(), 0)

    # Whitelist Tests
    def test_add_to_whitelist(self):
        # Add ingredient to whitelist
        self.user_pref.whitelist.add(self.ingredient1)
        self.assertIn(self.ingredient1, self.user_pref.whitelist.all())

    def test_remove_from_whitelist(self):
        # Add and remove an ingredient from the whitelist
        self.user_pref.whitelist.add(self.ingredient1)
        self.user_pref.whitelist.remove(self.ingredient1)
        self.assertNotIn(self.ingredient1, self.user_pref.whitelist.all())

    def test_multiple_ingredients_in_whitelist(self):
        # Add multiple ingredients to the whitelist
        self.user_pref.whitelist.add(self.ingredient1, self.ingredient2)
        self.assertIn(self.ingredient1, self.user_pref.whitelist.all())
        self.assertIn(self.ingredient2, self.user_pref.whitelist.all())

    def test_whitelist_filtering(self):
        # Test filtering recipes based on whitelist
        whitelist = ['Tomato']

        # Simulate whitelist filtering logic
        filtered_recipes = Recipe.objects.filter(
            recipeingredient__ingredient__name__in=whitelist
        )

        # Check that only recipes containing the ingredients in the whitelist are returned
        self.assertIn(self.recipe1, filtered_recipes)
        self.assertNotIn(
            self.recipe2, filtered_recipes
        )  # Onion Soup should be excluded
        self.assertNotIn(
            self.recipe3, filtered_recipes
        )  # Garlic Bread should be excluded

    def test_whitelist_with_no_results(self):
        # Test with whitelist that excludes all recipes
        whitelist = ['Carrot']  # Assuming 'Carrot' is not an ingredient in any recipe

        # Simulate whitelist filtering logic
        filtered_recipes = Recipe.objects.filter(
            recipeingredient__ingredient__name__in=whitelist
        )

        # Check that no recipes are returned since no recipe contains 'Carrot'
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
        RecipeIngredient.objects.create(
            recipe=self.recipe,
            ingredient=self.peanut,
            quantity="100g",
        )
        RecipeIngredient.objects.create(
            recipe=self.recipe,
            ingredient=self.flour,
            quantity="200g",
        )
        RecipeIngredient.objects.create(
            recipe=self.recipe,
            ingredient=self.sugar,
            quantity="150g",
        )

        # Create user and preferences
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass",
        )
        self.user_preference = UserPreference.objects.create(user=self.user)
        self.user_preference.blacklist.add(self.peanut)

    def test_recipe_ingredients_respects_blacklist(self):
        """Test that a recipe is correctly identified as containing blacklisted ingredients."""
        recipe_ingredients = RecipeIngredient.objects.filter(recipe=self.recipe)
        ingredient_ids = [ri.ingredient.id for ri in recipe_ingredients]
        blacklist_ids = self.user_preference.blacklist.values_list('id', flat=True)

        contains_blacklisted = any(
            ingredient in blacklist_ids for ingredient in ingredient_ids
        )
        self.assertTrue(contains_blacklisted)

    def test_recipe_without_blacklisted_ingredients(self):
        """Test that a recipe without blacklisted ingredients passes the filter."""
        self.user_preference.blacklist.clear()  # Clear blacklist to simulate no restriction
        blacklist_ids = self.user_preference.blacklist.values_list('id', flat=True)

        recipe_ingredients = RecipeIngredient.objects.filter(recipe=self.recipe)
        ingredient_ids = [ri.ingredient.id for ri in recipe_ingredients]

        contains_blacklisted = any(
            ingredient in blacklist_ids for ingredient in ingredient_ids
        )
        self.assertFalse(contains_blacklisted)


class RecipeListUnitTests(TestCase):
    def setUp(self):
        # Create test recipes
        self.recipe1 = Recipe.objects.create(
            title="Banana Bread",
            api_id="123",
            instructions="Mix and bake",
            calories=350,
            macros={"protein": 5, "carbs": 55, "fat": 12},
            tags=["baking", "dessert"],
        )

        self.recipe2 = Recipe.objects.create(
            title="Apple Pie",
            api_id="456",
            instructions="Make pie crust, fill with apples",
            calories=400,
            macros={"protein": 3, "carbs": 65, "fat": 15},
            tags=["baking", "dessert"],
        )

    def test_recipe_creation(self):
        """Test that recipes are created correctly"""
        self.assertEqual(self.recipe1.title, "Banana Bread")
        self.assertEqual(self.recipe2.title, "Apple Pie")
        self.assertEqual(Recipe.objects.count(), 2)

    def test_recipe_str_method(self):
        """Test the string representation of Recipe model"""
        self.assertEqual(str(self.recipe1), "Banana Bread")
        self.assertEqual(str(self.recipe2), "Apple Pie")

    def test_default_ordering(self):
        """Test that recipes are ordered alphabetically by default"""
        recipes = Recipe.objects.all()
        self.assertEqual(recipes[0].title, "Apple Pie")
        self.assertEqual(recipes[1].title, "Banana Bread")

    def test_average_rating_calculation(self):
        """Test the average rating calculation method"""
        # Create a user for ratings
        user = User.objects.create_user(username='testuser', password='12345')

        # Create ratings for recipe1
        Rating.objects.create(recipe=self.recipe1, user=user, value=4)
        Rating.objects.create(
            recipe=self.recipe1,
            user=User.objects.create_user(username='testuser2', password='12345'),
            value=5,
        )

        self.recipe1.update_average_rating()
        self.assertEqual(self.recipe1.average_rating, 4.5)

    def test_average_rating_no_ratings(self):
        """Test average rating calculation with no ratings"""
        self.recipe1.update_average_rating()
        self.assertEqual(self.recipe1.average_rating, 0.0)


class RecipeListIntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.recipe_list_url = reverse('recipes')

        # Create test recipes with different ratings
        self.recipe1 = Recipe.objects.create(
            title="Banana Bread",
            api_id="123",
            instructions="Mix and bake",
            average_rating=4.5,
        )

        self.recipe2 = Recipe.objects.create(
            title="Apple Pie",
            api_id="456",
            instructions="Make pie crust",
            average_rating=3.8,
        )

        self.recipe3 = Recipe.objects.create(
            title="Carrot Cake",
            api_id="789",
            instructions="Mix ingredients",
            average_rating=4.2,
        )

    def test_recipe_list_view_loads(self):
        """Test that the recipe list view loads successfully"""
        response = self.client.get(self.recipe_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookapp/recipe_list.html')
        self.assertContains(response, "All Recipes")

    def test_recipe_list_contains_all_recipes(self):
        """Test that all recipes are displayed in the list"""
        response = self.client.get(self.recipe_list_url)
        self.assertContains(response, "Banana Bread")
        self.assertContains(response, "Apple Pie")
        self.assertContains(response, "Carrot Cake")

    def test_recipe_list_sorting_name_asc(self):
        """Test alphabetical sorting (A-Z)"""
        response = self.client.get(f'{self.recipe_list_url}?sort=name')
        recipes = response.context['recipes']
        self.assertEqual(recipes[0].title, "Apple Pie")
        self.assertEqual(recipes[1].title, "Banana Bread")
        self.assertEqual(recipes[2].title, "Carrot Cake")

    def test_recipe_list_sorting_name_desc(self):
        """Test alphabetical sorting (Z-A)"""
        response = self.client.get(f'{self.recipe_list_url}?sort=name_desc')
        recipes = response.context['recipes']
        self.assertEqual(recipes[0].title, "Carrot Cake")
        self.assertEqual(recipes[1].title, "Banana Bread")
        self.assertEqual(recipes[2].title, "Apple Pie")

    def test_recipe_list_sorting_rating(self):
        """Test rating sorting (High to Low)"""
        response = self.client.get(f'{self.recipe_list_url}?sort=rating')
        recipes = response.context['recipes']
        self.assertEqual(recipes[0].title, "Banana Bread")  # 4.5
        self.assertEqual(recipes[1].title, "Carrot Cake")   # 4.2
        self.assertEqual(recipes[2].title, "Apple Pie")     # 3.8

    def test_recipe_list_sorting_rating_asc(self):
        """Test rating sorting (Low to High)"""
        response = self.client.get(f'{self.recipe_list_url}?sort=rating_asc')
        recipes = response.context['recipes']
        self.assertEqual(recipes[0].title, "Apple Pie")     # 3.8
        self.assertEqual(recipes[1].title, "Carrot Cake")   # 4.2
        self.assertEqual(recipes[2].title, "Banana Bread")  # 4.5

    def test_recipe_list_pagination(self):
        """Test that pagination works correctly"""
        # Create more recipes to trigger pagination
        for i in range(10):
            Recipe.objects.create(
                title=f"Test Recipe {i}",
                api_id=f"test{i}",
                instructions="Test instructions",
                average_rating=3.0,
            )

        # Test first page
        response = self.client.get(self.recipe_list_url)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'])

        # Test page navigation
        response = self.client.get(f'{self.recipe_list_url}?page=2')
        self.assertEqual(response.status_code, 200)


class IngredientModelTest(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(
            name="Tomato",
            tags=["vegetarian", "gluten-free"],
        )

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
            tags=["quick", "easy"],
        )

        RecipeIngredient.objects.create(
            recipe=self.recipe,
            ingredient=self.ingredient1,
            quantity="2 cups",
        )
        RecipeIngredient.objects.create(
            recipe=self.recipe,
            ingredient=self.ingredient2,
            quantity="1 cup",
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, "Tomato Cheese Salad")
        self.assertEqual(self.recipe.api_id, "12345")
        self.assertEqual(self.recipe.instructions, "Mix tomatoes and cheese.")
        self.assertEqual(self.recipe.calories, 200)
        self.assertEqual(self.recipe.macros, {"protein": 10, "carbs": 15, "fat": 10})
        self.assertEqual(self.recipe.tags, ["quick", "easy"])
        self.assertEqual(str(self.recipe), "Tomato Cheese Salad")
        self.assertIn(
            self.ingredient1,
            [ri.ingredient for ri in self.recipe.recipeingredient_set.all()],
        )
        self.assertIn(
            self.ingredient2,
            [ri.ingredient for ri in self.recipe.recipeingredient_set.all()],
        )

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
            tags=["quick", "easy"],
        )
        self.rating = Rating.objects.create(
            user=self.user,
            recipe=self.recipe,
            value=5,
            review="Delicious!",
        )

    def test_rating_creation(self):
        self.assertEqual(self.rating.user.username, "testuser")
        self.assertEqual(self.rating.recipe.title, "Tomato Cheese Salad")
        self.assertEqual(self.rating.value, 5)
        self.assertEqual(self.rating.review, "Delicious!")
        self.assertEqual(
            str(self.rating), "testuser rated Tomato Cheese Salad as 5"
        )

    def test_update_average_rating(self):
        self.recipe.update_average_rating()
        self.assertEqual(self.recipe.average_rating, 5.0)


class FavoriteRecipeTests(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

        # Create a test recipe using the correct fields
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            api_id='test-api-id',
            instructions='Test description',
            calories=200,
            macros={},
            tags=[],
        )

    def test_toggle_favorite_add(self):
        # Send POST request to toggle favorite for the recipe
        response = self.client.post(
            reverse('toggle_favorite', args=[self.recipe.id])
        )

        # Check if the response is a redirect to the recipe detail page
        self.assertRedirects(
            response,
            reverse('recipe_detail', args=[self.recipe.id])
        )

        # Verify the favorite is added
        self.assertTrue(
            FavoriteRecipe.objects.filter(user=self.user, recipe=self.recipe).exists()
        )

    def test_toggle_favorite_remove(self):
        # First, create a favorite entry for the test
        FavoriteRecipe.objects.create(user=self.user, recipe=self.recipe)

        # Send POST request to toggle favorite for the recipe
        response = self.client.post(
            reverse('toggle_favorite', args=[self.recipe.id])
        )

        # Check if the response is a redirect to the recipe detail page
        self.assertRedirects(
            response,
            reverse('recipe_detail', args=[self.recipe.id])
        )

        # Verify the favorite is removed
        self.assertFalse(
            FavoriteRecipe.objects.filter(user=self.user, recipe=self.recipe).exists()
        )


class CreateRecipeTests(TestCase):
    def test_create_recipe(self):
        # Adjust form data to match the RecipeForm requirements
        form_data = {
            'title': 'Test Recipe',
            'description': 'This is a test recipe.',
            'instructions': 'Mix ingredients and cook.',  # Required field
            'image': 'http://example.com/image.jpg',      # Optional
            'calories': 200,                              # Required field
            'protein': 10,                                # Required field
            'carbs': 30,                                  # Required field
            'fat': 5,                                     # Required field
            'tags': 'easy, dinner',                       # Required field
        }

        # Send POST request to create a recipe
        response = self.client.post(reverse('create_recipe'), form_data)

        # Check if the response redirects to the add_ingredients view
        self.assertEqual(response.status_code, 302)

        # Check if the recipe was created
        recipe = Recipe.objects.first()
        self.assertIsNotNone(recipe)
        self.assertEqual(recipe.title, 'Test Recipe')
        self.assertIsNotNone(recipe.api_id)
