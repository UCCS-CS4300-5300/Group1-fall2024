from django.test import TestCase
from django.contrib.auth.models import User
from cookapp.models import Ingredient, Recipe, UserPreference

class IngredientModelTest(TestCase):
    def setUp(self):
        # Create an Ingredient instance for testing
        self.ingredient = Ingredient.objects.create(name="Tomato", tags=["vegetarian", "gluten-free"])

    def test_ingredient_creation(self):
        # Test the creation of the Ingredient instance
        self.assertEqual(self.ingredient.name, "Tomato", "Ingredient name should be 'Tomato'")
        self.assertEqual(self.ingredient.tags, ["vegetarian", "gluten-free"], "Ingredient tags should be ['vegetarian', 'gluten-free']")
        self.assertEqual(str(self.ingredient), "Tomato", "String representation of the ingredient should be 'Tomato'")

    def test_ingredient_ordering(self):
        # Test the ordering of Ingredient instances
        ingredient2 = Ingredient.objects.create(name="Apple")
        ingredients = Ingredient.objects.all()
        self.assertEqual(ingredients[0].name, "Apple", "First ingredient should be 'Apple' due to ordering")
        self.assertEqual(ingredients[1].name, "Tomato", "Second ingredient should be 'Tomato' due to ordering")

class RecipeModelTest(TestCase):
    def setUp(self):
        # Create Ingredient instances for testing
        self.ingredient1 = Ingredient.objects.create(name="Tomato")
        self.ingredient2 = Ingredient.objects.create(name="Cheese")
        
        # Create a Recipe instance for testing
        self.recipe = Recipe.objects.create(
            title="Tomato Cheese Salad",
            api_id="12345",
            instructions="Mix tomatoes and cheese.",
            calories=200,
            macros={"protein": 10, "carbs": 15, "fat": 10},
            tags=["quick", "easy"]
        )
        
        # Add ingredients to the recipe
        self.recipe.ingredients.add(self.ingredient1, self.ingredient2)

    def test_recipe_creation(self):
        # Test the creation of the Recipe instance
        self.assertEqual(self.recipe.title, "Tomato Cheese Salad", "Recipe title should be 'Tomato Cheese Salad'")
        self.assertEqual(self.recipe.api_id, "12345", "Recipe API ID should be '12345'")
        self.assertEqual(self.recipe.instructions, "Mix tomatoes and cheese.", "Recipe instructions should be 'Mix tomatoes and cheese.'")
        self.assertEqual(self.recipe.calories, 200, "Recipe calories should be 200")
        self.assertEqual(self.recipe.macros, {"protein": 10, "carbs": 15, "fat": 10}, "Recipe macros should be {'protein': 10, 'carbs': 15, 'fat': 10}")
        self.assertEqual(self.recipe.tags, ["quick", "easy"], "Recipe tags should be ['quick', 'easy']")
        self.assertEqual(str(self.recipe), "Tomato Cheese Salad", "String representation of the recipe should be 'Tomato Cheese Salad'")
        self.assertIn(self.ingredient1, self.recipe.ingredients.all(), "Ingredient 'Tomato' should be in the recipe ingredients")
        self.assertIn(self.ingredient2, self.recipe.ingredients.all(), "Ingredient 'Cheese' should be in the recipe ingredients")

    def test_recipe_ordering(self):
        # Test the ordering of Recipe instances
        recipe2 = Recipe.objects.create(title="Apple Pie", api_id="67890")
        recipes = Recipe.objects.all()
        self.assertEqual(recipes[0].title, "Apple Pie", "First recipe should be 'Apple Pie' due to ordering")
        self.assertEqual(recipes[1].title, "Tomato Cheese Salad", "Second recipe should be 'Tomato Cheese Salad' due to ordering")

class UserPreferenceModelTest(TestCase):
    def setUp(self):
        # Create a User instance for testing
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        # Create Ingredient instances for testing
        self.ingredient1 = Ingredient.objects.create(name="Tomato")
        self.ingredient2 = Ingredient.objects.create(name="Cheese")
        
        # Create a UserPreference instance for testing
        self.user_preference = UserPreference.objects.create(user=self.user)
        
        # Add ingredients to the whitelist and blacklist
        self.user_preference.whitelist.add(self.ingredient1)
        self.user_preference.blacklist.add(self.ingredient2)

    def test_user_preference_creation(self):
        # Test the creation of the UserPreference instance
        self.assertEqual(self.user_preference.user.username, "testuser", "User preference should be associated with 'testuser'")
        self.assertIn(self.ingredient1, self.user_preference.whitelist.all(), "Ingredient 'Tomato' should be in the whitelist")
        self.assertIn(self.ingredient2, self.user_preference.blacklist.all(), "Ingredient 'Cheese' should be in the blacklist")
        self.assertEqual(str(self.user_preference), "testuser's preferences", "String representation of the user preference should be 'testuser's preferences'")