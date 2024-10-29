from django.db import models
from django.contrib.auth.models import User

# Ingredient Model
class Ingredient(models.Model):
    """
    Model representing an ingredient.

    Fields:
        name: CharField representing the name of the ingredient
        tags: JSONField representing the tags associated with the ingredient ex. ['vegetarian', 'gluten-free', etc.]
    """
    name = models.CharField(max_length=100)
    tags = models.JSONField(null=True, blank=True)  # Store tags as JSON

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # orders the ingredients by name A-Z


# model for dietary restrictions (allergies, vegan/vegetarian)
class Diets(models.Model):
    """
    Model representing diets that restrict options.

    Fields:
        name: CharField representing the restriction
        blacklist: ManyToManyField representing the blacklisted ingredients related to the dietary restriction (relationship to Ingredient model)
    """
    name = models.CharField(max_length=50)
    blacklist = models.ManyToManyField(Ingredient, related_name='diet_blacklist')

    def __str__(self):
        return self.name


# model to store recipes and their details
class Recipe(models.Model):
    """
    Model representing a recipe.

    Fields:
        title: CharField representing the title of the recipe
        api_id: CharField representing the API ID of the recipe
        instructions: TextField representing the instructions to make the recipe
        image: URLField representing the image URL of the recipe
        calories: IntegerField representing the total calories in the recipe
        macros: JSONField representing the macronutrients in the recipe
        tags: JSONField representing the tags associated with the recipe ex. ['quick', 'easy', 'low-carb', etc.]
    """
    title = models.CharField(max_length=200)
    api_id = models.CharField(max_length=100, unique=True)  # Reference to the API ID
    instructions = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    macros = models.JSONField(null=True, blank=True)  # Store macros as JSON
    tags = models.JSONField(null=True, blank=True)  # Store tags as JSON

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']  # orders the recipes by title A-Z

# Intermediary Model for Recipe and Ingredient
class RecipeIngredient(models.Model):
    """
    Intermediary model representing the quantity of each ingredient in a recipe.

    Fields:
        recipe: ForeignKey to the Recipe model
        ingredient: ForeignKey to the Ingredient model
        quantity: CharField representing the quantity of the ingredient
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.title}"

    class Meta:
        unique_together = ('recipe', 'ingredient')

# UserPreference Model
class UserPreference(models.Model):
    """
    Model representing user preferences for ingredients.

    Fields:
        user: OneToOneField representing the user (relationship to User model)
        whitelist: ManyToManyField representing the whitelisted ingredients (relationship to Ingredient model)
        blacklist: ManyToManyField representing the blacklisted ingredients (relationship to Ingredient model)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    whitelist = models.ManyToManyField(Ingredient, related_name='whitelisted_by', blank=True)
    blacklist = models.ManyToManyField(Ingredient, related_name='blacklisted_by', blank=True)

    def __str__(self):
        return f"{self.user.username}'s preferences"

# model for favorite 
class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'recipe')  # Prevent duplicate entries

# maybe implement later
# class FavoriteRecipe(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.user.username} - {self.recipe.title}"
#
# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     comment = models.TextField()
#
#     def __str__(self):
#         return f"{self.user.username} - {self.recipe.title} - {self.rating}"