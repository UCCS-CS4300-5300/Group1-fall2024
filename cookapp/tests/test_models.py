from django.test import TestCase
from django.contrib.auth.models import User
from cookapp.models import Ingredient, Recipe, UserPreference, RecipeIngredient, FavoriteRecipe

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
        
        # Create RecipeIngredient instances to associate ingredients with the recipe
        self.recipe_ingredient1 = RecipeIngredient.objects.create(
            recipe=self.recipe,
            ingredient=self.ingredient1,
            quantity="2 cups"
        )
        self.recipe_ingredient2 = RecipeIngredient.objects.create(
            recipe=self.recipe,
            ingredient=self.ingredient2,
            quantity="1 cup"
        )

    def test_recipe_creation(self):
        # Test the creation of the Recipe instance
        self.assertEqual(self.recipe.title, "Tomato Cheese Salad")
        self.assertEqual(self.recipe.api_id, "12345")
        self.assertEqual(self.recipe.instructions, "Mix tomatoes and cheese.")
        self.assertEqual(self.recipe.calories, 200)
        self.assertEqual(self.recipe.macros, {"protein": 10, "carbs": 15, "fat": 10})
        self.assertEqual(self.recipe.tags, ["quick", "easy"])
        self.assertEqual(str(self.recipe), "Tomato Cheese Salad")
        
        # Test that the RecipeIngredient instances are associated correctly
        recipe_ingredients = RecipeIngredient.objects.filter(recipe=self.recipe)
        self.assertEqual(recipe_ingredients.count(), 2)
        ingredients = [ri.ingredient for ri in recipe_ingredients]
        self.assertIn(self.ingredient1, ingredients)
        self.assertIn(self.ingredient2, ingredients)

    def test_recipe_ordering(self):
        # Test the ordering of Recipe instances
        recipe2 = Recipe.objects.create(title="Apple Pie", api_id="67890")
        recipes = Recipe.objects.all()
        self.assertEqual(recipes[0].title, "Apple Pie", "First recipe should be 'Apple Pie' due to ordering")
        self.assertEqual(recipes[1].title, "Tomato Cheese Salad", "Second recipe should be 'Tomato Cheese Salad' due to ordering")


class RecipeIngredientModelTest(TestCase):
    def setUp(self):
        # Create Ingredient and Recipe instances for testing
        self.ingredient = Ingredient.objects.create(name="Sugar")
        self.recipe = Recipe.objects.create(
            title="Sugar Syrup",
            api_id="54321",
            instructions="Mix sugar with water.",
            calories=100,
            macros={"carbs": 25},
            tags=["sweet", "easy"]
        )
        
        # Create a RecipeIngredient instance
        self.recipe_ingredient = RecipeIngredient.objects.create(
            recipe=self.recipe,
            ingredient=self.ingredient,
            quantity="1 cup"
        )

    def test_recipe_ingredient_creation(self):
        # Test the creation of the RecipeIngredient instance
        self.assertEqual(self.recipe_ingredient.recipe, self.recipe)
        self.assertEqual(self.recipe_ingredient.ingredient, self.ingredient)
        self.assertEqual(self.recipe_ingredient.quantity, "1 cup")
        expected_str = f"1 cup of {self.ingredient.name} in {self.recipe.title}"
        self.assertEqual(str(self.recipe_ingredient), expected_str)

    def test_unique_together_constraint(self):
        # Test that the unique_together constraint works
        with self.assertRaises(Exception):
            RecipeIngredient.objects.create(
                recipe=self.recipe,
                ingredient=self.ingredient,
                quantity="2 cups"
            )

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

class FavoriteRecipeModelTest(TestCase):
    def setUp(self):
        # Create User and Recipe instances for testing
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.recipe = Recipe.objects.create(
            title="Tomato Cheese Salad",
            api_id="12345",
            instructions="Mix tomatoes and cheese.",
            calories=200,
            macros={"protein": 10, "carbs": 15, "fat": 10},
            tags=["quick", "easy"]
        )

    def test_favorite_recipe_creation(self):
        # Test that a FavoriteRecipe instance can be created
        favorite = FavoriteRecipe.objects.create(user=self.user, recipe=self.recipe)
        self.assertEqual(favorite.user, self.user, "User should be correctly associated with the favorite")
        self.assertEqual(favorite.recipe, self.recipe, "Recipe should be correctly associated with the favorite")
        
        # Use the default string representation
        self.assertEqual(str(favorite), f"FavoriteRecipe object ({favorite.id})", "String representation should match the default")
        
    def test_unique_together_constraint(self):
        # Test that the unique_together constraint works
        FavoriteRecipe.objects.create(user=self.user, recipe=self.recipe)
        
        # Try to create the same favorite again, should raise IntegrityError
        with self.assertRaises(Exception):
            FavoriteRecipe.objects.create(user=self.user, recipe=self.recipe)

