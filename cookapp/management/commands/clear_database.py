from django.core.management.base import BaseCommand
from cookapp.models import Recipe, Ingredient, RecipeIngredient

class Command(BaseCommand):
    help = 'Clears the database of all recipes, ingredients, and recipe-ingredient relationships'

    def handle(self, *args, **options):
        RecipeIngredient.objects.all().delete()
        Recipe.objects.all().delete()
        Ingredient.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared the database.'))
