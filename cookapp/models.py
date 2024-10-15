from email.mime import image
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# model for storing ingredients
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
        ordering = ['name'] # orders the ingredients by name A-Z

# model to store recipes and their details
class Recipe(models.Model):
    """
    Model representing a recipe.
    an ingredient can be used in multiple recipes and a recipe can have multiple ingredients (many-to-many relationship)

    Fields:
        title: CharField representing the title of the recipe
        ingredients: ManyToManyField representing the ingredients (relationship to Ingredient model)
        instructions: TextField representing the instructions to make the recipe
        calories: IntegerField representing the total calories in the recipe
        macros: JSONField representing the macronutrients in the recipe
        image: url to the image of the recipe
        tags: JSONField representing the tags associated with the recipe ex. ['quick', 'easy', 'low-carb', etc.]

    Note: 
        The API ID is stored as a CharField to allow for the possibility of using multiple APIs or non-repeating IDs.
        We can maybe use logic in views.py to assign tags based stuff like ingredients, calories, number of ingredients, etc.
    """
    title = models.CharField(max_length=200)
    api_id = models.CharField(max_length=100, unique=True)  # Reference to the API ID
    ingredients = models.ManyToManyField(Ingredient) # Many-to-many relationship with Ingredient model
    instructions = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    macros = models.JSONField(null=True, blank=True)  # Store macros as JSON
    tags = models.JSONField(null=True, blank=True)  # Store tags as JSON

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title'] # orders the recipes by title A-Z

# model to store whitelist and blacklist
class UserPreference(models.Model):
    """
    Model representing user preferences for ingredients.
    a user can have multiple whitelisted and blacklisted ingredients (many-to-many relationship)

    Fields:
        user: OneToOneField representing the user (relationship to User model)
        whitelist: ManyToManyField representing the whitelisted ingredients (relationship to Ingredient model)
        blacklist: ManyToManyField representing the blacklisted ingredients (relationship to Ingredient model)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    whitelist = models.ManyToManyField(Ingredient, related_name='whitelisted_by')
    blacklist = models.ManyToManyField(Ingredient, related_name='blacklisted_by')

    def __str__(self):
        return f"{self.user.username}'s preferences"
    

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