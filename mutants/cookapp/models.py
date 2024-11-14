
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


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

    def xǁIngredientǁ__str____mutmut_orig(self):
        return self.name

    xǁIngredientǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIngredientǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁIngredientǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁIngredientǁ__str____mutmut_orig)
    xǁIngredientǁ__str____mutmut_orig.__name__ = 'xǁIngredientǁ__str__'



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

    def xǁDietsǁ__str____mutmut_orig(self):
        return self.name

    xǁDietsǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDietsǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁDietsǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁDietsǁ__str____mutmut_orig)
    xǁDietsǁ__str____mutmut_orig.__name__ = 'xǁDietsǁ__str__'




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
    average_rating = models.FloatField(default=0.0)  # New field for average rating

    def xǁRecipeǁupdate_average_rating__mutmut_orig(self):
        ratings = self.ratings.all()
        if ratings.exists():
            self.average_rating = sum(rating.value for rating in ratings) / ratings.count()
        else:
            self.average_rating = 0.0
        self.save()

    def xǁRecipeǁupdate_average_rating__mutmut_1(self):
        ratings = None
        if ratings.exists():
            self.average_rating = sum(rating.value for rating in ratings) / ratings.count()
        else:
            self.average_rating = 0.0
        self.save()

    def xǁRecipeǁupdate_average_rating__mutmut_2(self):
        ratings = self.ratings.all()
        if ratings.exists():
            self.average_rating = sum(rating.value for rating in ratings) * ratings.count()
        else:
            self.average_rating = 0.0
        self.save()

    def xǁRecipeǁupdate_average_rating__mutmut_3(self):
        ratings = self.ratings.all()
        if ratings.exists():
            self.average_rating = None
        else:
            self.average_rating = 0.0
        self.save()

    def xǁRecipeǁupdate_average_rating__mutmut_4(self):
        ratings = self.ratings.all()
        if ratings.exists():
            self.average_rating = sum(rating.value for rating in ratings) / ratings.count()
        else:
            self.average_rating = 1.0
        self.save()

    def xǁRecipeǁupdate_average_rating__mutmut_5(self):
        ratings = self.ratings.all()
        if ratings.exists():
            self.average_rating = sum(rating.value for rating in ratings) / ratings.count()
        else:
            self.average_rating = None
        self.save()

    xǁRecipeǁupdate_average_rating__mutmut_mutants = {
    'xǁRecipeǁupdate_average_rating__mutmut_1': xǁRecipeǁupdate_average_rating__mutmut_1, 
        'xǁRecipeǁupdate_average_rating__mutmut_2': xǁRecipeǁupdate_average_rating__mutmut_2, 
        'xǁRecipeǁupdate_average_rating__mutmut_3': xǁRecipeǁupdate_average_rating__mutmut_3, 
        'xǁRecipeǁupdate_average_rating__mutmut_4': xǁRecipeǁupdate_average_rating__mutmut_4, 
        'xǁRecipeǁupdate_average_rating__mutmut_5': xǁRecipeǁupdate_average_rating__mutmut_5
    }

    def update_average_rating(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeǁupdate_average_rating__mutmut_orig"), object.__getattribute__(self, "xǁRecipeǁupdate_average_rating__mutmut_mutants"), *args, **kwargs)
        return result 

    update_average_rating.__signature__ = _mutmut_signature(xǁRecipeǁupdate_average_rating__mutmut_orig)
    xǁRecipeǁupdate_average_rating__mutmut_orig.__name__ = 'xǁRecipeǁupdate_average_rating'



    def xǁRecipeǁ__str____mutmut_orig(self):
        return self.title

    xǁRecipeǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁRecipeǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁRecipeǁ__str____mutmut_orig)
    xǁRecipeǁ__str____mutmut_orig.__name__ = 'xǁRecipeǁ__str__'



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

    def xǁRecipeIngredientǁ__str____mutmut_orig(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.title}"

    xǁRecipeIngredientǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeIngredientǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁRecipeIngredientǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁRecipeIngredientǁ__str____mutmut_orig)
    xǁRecipeIngredientǁ__str____mutmut_orig.__name__ = 'xǁRecipeIngredientǁ__str__'



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

    def xǁUserPreferenceǁ__str____mutmut_orig(self):
        return f"{self.user.username}'s preferences"

    xǁUserPreferenceǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserPreferenceǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁUserPreferenceǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁUserPreferenceǁ__str____mutmut_orig)
    xǁUserPreferenceǁ__str____mutmut_orig.__name__ = 'xǁUserPreferenceǁ__str__'



# model for favorite 
class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'recipe')  # Prevent duplicate entries

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(null=False)
    review = models.TextField(blank=True, null=True)  # Review text
    class Meta:
        unique_together = ('user', 'recipe')
    def xǁRatingǁ__str____mutmut_orig(self):
        return f"{self.user.username} rated {self.recipe.title} as {self.value}"

    xǁRatingǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRatingǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁRatingǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁRatingǁ__str____mutmut_orig)
    xǁRatingǁ__str____mutmut_orig.__name__ = 'xǁRatingǁ__str__'


