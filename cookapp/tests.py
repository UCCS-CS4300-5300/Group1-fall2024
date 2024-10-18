from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import *

class UserTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            username = "test_user",
            email = "test@user.com",
            password = "test1234",
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
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(
            title='Onion Soup',
            api_id='api_002',
            instructions='Cook onions.',
            calories=100,
        )
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(
            title='Garlic Bread',
            api_id='api_003',
            instructions='Bake garlic in bread.',
            calories=200,
        )
        self.recipe3.ingredients.add(self.ingredient3)

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
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='api_002', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

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
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2, filtered_recipes)
        self.assertIn(self.recipe1, filtered_recipes)
        self.assertIn(self.recipe3, filtered_recipes)

    def test_blacklist_with_no_results(self):
        # Test with blacklist that excludes all recipes
        blacklist = ['Onion', 'Tomato', 'Garlic']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that no recipes are returned
        self.assertEqual(filtered_recipes.count(), 0)

        
