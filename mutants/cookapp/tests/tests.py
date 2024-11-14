
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


from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from cookapp.models import *

class UserTestCase(TestCase):
    def xǁUserTestCaseǁsetUp__mutmut_orig(self):
        self.test_user = User.objects.create(
            username = "test_user",
            email = "test@user.com",
            password = "test1234",
        )
    def xǁUserTestCaseǁsetUp__mutmut_1(self):
        self.test_user = User.objects.create(
            username = "XXtest_userXX",
            email = "test@user.com",
            password = "test1234",
        )
    def xǁUserTestCaseǁsetUp__mutmut_2(self):
        self.test_user = User.objects.create(
            username = "test_user",
            email = "XXtest@user.comXX",
            password = "test1234",
        )
    def xǁUserTestCaseǁsetUp__mutmut_3(self):
        self.test_user = User.objects.create(
            username = "test_user",
            email = "test@user.com",
            password = "XXtest1234XX",
        )
    def xǁUserTestCaseǁsetUp__mutmut_4(self):
        self.test_user = User.objects.create(
            email = "test@user.com",
            password = "test1234",
        )
    def xǁUserTestCaseǁsetUp__mutmut_5(self):
        self.test_user = User.objects.create(
            username = "test_user",
            password = "test1234",
        )
    def xǁUserTestCaseǁsetUp__mutmut_6(self):
        self.test_user = User.objects.create(
            username = "test_user",
            email = "test@user.com",
        )
    def xǁUserTestCaseǁsetUp__mutmut_7(self):
        self.test_user = None

    xǁUserTestCaseǁsetUp__mutmut_mutants = {
    'xǁUserTestCaseǁsetUp__mutmut_1': xǁUserTestCaseǁsetUp__mutmut_1, 
        'xǁUserTestCaseǁsetUp__mutmut_2': xǁUserTestCaseǁsetUp__mutmut_2, 
        'xǁUserTestCaseǁsetUp__mutmut_3': xǁUserTestCaseǁsetUp__mutmut_3, 
        'xǁUserTestCaseǁsetUp__mutmut_4': xǁUserTestCaseǁsetUp__mutmut_4, 
        'xǁUserTestCaseǁsetUp__mutmut_5': xǁUserTestCaseǁsetUp__mutmut_5, 
        'xǁUserTestCaseǁsetUp__mutmut_6': xǁUserTestCaseǁsetUp__mutmut_6, 
        'xǁUserTestCaseǁsetUp__mutmut_7': xǁUserTestCaseǁsetUp__mutmut_7
    }

    def setUp(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserTestCaseǁsetUp__mutmut_orig"), object.__getattribute__(self, "xǁUserTestCaseǁsetUp__mutmut_mutants"), *args, **kwargs)
        return result 

    setUp.__signature__ = _mutmut_signature(xǁUserTestCaseǁsetUp__mutmut_orig)
    xǁUserTestCaseǁsetUp__mutmut_orig.__name__ = 'xǁUserTestCaseǁsetUp'



    def xǁUserTestCaseǁtest_user_created__mutmut_orig(self):
        self.assertEqual(self.test_user.username, "test_user")
        self.assertEqual(self.test_user.password, "test1234")
        self.assertEqual(self.test_user.email, "test@user.com")

    def xǁUserTestCaseǁtest_user_created__mutmut_1(self):
        self.assertEqual(self.test_user.username, "XXtest_userXX")
        self.assertEqual(self.test_user.password, "test1234")
        self.assertEqual(self.test_user.email, "test@user.com")

    def xǁUserTestCaseǁtest_user_created__mutmut_2(self):
        self.assertEqual(self.test_user.username, "test_user")
        self.assertEqual(self.test_user.password, "XXtest1234XX")
        self.assertEqual(self.test_user.email, "test@user.com")

    def xǁUserTestCaseǁtest_user_created__mutmut_3(self):
        self.assertEqual(self.test_user.username, "test_user")
        self.assertEqual(self.test_user.password, "test1234")
        self.assertEqual(self.test_user.email, "XXtest@user.comXX")

    xǁUserTestCaseǁtest_user_created__mutmut_mutants = {
    'xǁUserTestCaseǁtest_user_created__mutmut_1': xǁUserTestCaseǁtest_user_created__mutmut_1, 
        'xǁUserTestCaseǁtest_user_created__mutmut_2': xǁUserTestCaseǁtest_user_created__mutmut_2, 
        'xǁUserTestCaseǁtest_user_created__mutmut_3': xǁUserTestCaseǁtest_user_created__mutmut_3
    }

    def test_user_created(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserTestCaseǁtest_user_created__mutmut_orig"), object.__getattribute__(self, "xǁUserTestCaseǁtest_user_created__mutmut_mutants"), *args, **kwargs)
        return result 

    test_user_created.__signature__ = _mutmut_signature(xǁUserTestCaseǁtest_user_created__mutmut_orig)
    xǁUserTestCaseǁtest_user_created__mutmut_orig.__name__ = 'xǁUserTestCaseǁtest_user_created'




class IndexTestCase(TestCase):
    def xǁIndexTestCaseǁtest_index_view__mutmut_orig(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookapp/index.html')
    def xǁIndexTestCaseǁtest_index_view__mutmut_1(self):
        client = None
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookapp/index.html')
    def xǁIndexTestCaseǁtest_index_view__mutmut_2(self):
        client = Client()
        response = client.get(reverse('XXindexXX'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookapp/index.html')
    def xǁIndexTestCaseǁtest_index_view__mutmut_3(self):
        client = Client()
        response = None
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookapp/index.html')
    def xǁIndexTestCaseǁtest_index_view__mutmut_4(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 201)
        self.assertTemplateUsed(response, 'cookapp/index.html')
    def xǁIndexTestCaseǁtest_index_view__mutmut_5(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(None, 'cookapp/index.html')
    def xǁIndexTestCaseǁtest_index_view__mutmut_6(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'XXcookapp/index.htmlXX')
    def xǁIndexTestCaseǁtest_index_view__mutmut_7(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed( 'cookapp/index.html')

    xǁIndexTestCaseǁtest_index_view__mutmut_mutants = {
    'xǁIndexTestCaseǁtest_index_view__mutmut_1': xǁIndexTestCaseǁtest_index_view__mutmut_1, 
        'xǁIndexTestCaseǁtest_index_view__mutmut_2': xǁIndexTestCaseǁtest_index_view__mutmut_2, 
        'xǁIndexTestCaseǁtest_index_view__mutmut_3': xǁIndexTestCaseǁtest_index_view__mutmut_3, 
        'xǁIndexTestCaseǁtest_index_view__mutmut_4': xǁIndexTestCaseǁtest_index_view__mutmut_4, 
        'xǁIndexTestCaseǁtest_index_view__mutmut_5': xǁIndexTestCaseǁtest_index_view__mutmut_5, 
        'xǁIndexTestCaseǁtest_index_view__mutmut_6': xǁIndexTestCaseǁtest_index_view__mutmut_6, 
        'xǁIndexTestCaseǁtest_index_view__mutmut_7': xǁIndexTestCaseǁtest_index_view__mutmut_7
    }

    def test_index_view(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁIndexTestCaseǁtest_index_view__mutmut_orig"), object.__getattribute__(self, "xǁIndexTestCaseǁtest_index_view__mutmut_mutants"), *args, **kwargs)
        return result 

    test_index_view.__signature__ = _mutmut_signature(xǁIndexTestCaseǁtest_index_view__mutmut_orig)
    xǁIndexTestCaseǁtest_index_view__mutmut_orig.__name__ = 'xǁIndexTestCaseǁtest_index_view'



# Integration tests for Blacklist
class RecipeSearchIntegrationTests(TestCase):
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_orig(self):
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_1(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='XXTomatoXX')
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_2(self):
        # Create some ingredients
        self.ingredient1 = None
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_3(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='XXOnionXX')
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_4(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = None
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_5(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='XXGarlicXX')

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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_6(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = None

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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_7(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(
            title='XXTomato SoupXX',
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_8(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(
            title='Tomato Soup',
            api_id='XXapi_001XX',
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_9(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(
            title='Tomato Soup',
            api_id='api_001',
            instructions='XXBoil the tomatoes.XX',
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_10(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(
            title='Tomato Soup',
            api_id='api_001',
            instructions='Boil the tomatoes.',
            calories=151,
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_11(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_12(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(
            title='Tomato Soup',
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_13(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(
            title='Tomato Soup',
            api_id='api_001',
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_14(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(
            title='Tomato Soup',
            api_id='api_001',
            instructions='Boil the tomatoes.',
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_15(self):
        # Create some ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = None
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_16(self):
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
            title='XXOnion SoupXX',
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_17(self):
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
            api_id='XXapi_002XX',
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_18(self):
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
            instructions='XXCook onions.XX',
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_19(self):
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
            calories=101,
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_20(self):
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_21(self):
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_22(self):
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_23(self):
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_24(self):
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

        self.recipe2 = None
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
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_25(self):
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
            title='XXGarlic BreadXX',
            api_id='api_003',
            instructions='Bake garlic in bread.',
            calories=200,
        )
        self.recipe3.ingredients.add(self.ingredient3)

        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_26(self):
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
            api_id='XXapi_003XX',
            instructions='Bake garlic in bread.',
            calories=200,
        )
        self.recipe3.ingredients.add(self.ingredient3)

        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_27(self):
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
            instructions='XXBake garlic in bread.XX',
            calories=200,
        )
        self.recipe3.ingredients.add(self.ingredient3)

        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_28(self):
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
            calories=201,
        )
        self.recipe3.ingredients.add(self.ingredient3)

        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_29(self):
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
            api_id='api_003',
            instructions='Bake garlic in bread.',
            calories=200,
        )
        self.recipe3.ingredients.add(self.ingredient3)

        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_30(self):
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
            instructions='Bake garlic in bread.',
            calories=200,
        )
        self.recipe3.ingredients.add(self.ingredient3)

        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_31(self):
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
            calories=200,
        )
        self.recipe3.ingredients.add(self.ingredient3)

        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_32(self):
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
        )
        self.recipe3.ingredients.add(self.ingredient3)

        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_33(self):
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

        self.recipe3 = None
        self.recipe3.ingredients.add(self.ingredient3)

        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_34(self):
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
        self.user = User.objects.create_user(username='XXtestuserXX', password='testpass')
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_35(self):
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
        self.user = User.objects.create_user(username='testuser', password='XXtestpassXX')
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_36(self):
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
        self.user = User.objects.create_user( password='testpass')
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_37(self):
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
        self.user = User.objects.create_user(username='testuser',)
    def xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_38(self):
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
        self.user = None

    xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_mutants = {
    'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_1': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_1, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_2': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_2, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_3': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_3, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_4': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_4, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_5': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_5, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_6': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_6, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_7': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_7, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_8': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_8, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_9': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_9, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_10': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_10, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_11': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_11, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_12': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_12, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_13': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_13, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_14': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_14, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_15': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_15, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_16': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_16, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_17': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_17, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_18': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_18, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_19': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_19, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_20': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_20, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_21': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_21, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_22': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_22, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_23': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_23, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_24': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_24, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_25': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_25, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_26': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_26, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_27': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_27, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_28': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_28, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_29': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_29, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_30': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_30, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_31': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_31, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_32': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_32, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_33': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_33, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_34': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_34, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_35': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_35, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_36': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_36, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_37': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_37, 
        'xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_38': xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_38
    }

    def setUp(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_orig"), object.__getattribute__(self, "xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_mutants"), *args, **kwargs)
        return result 

    setUp.__signature__ = _mutmut_signature(xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_orig)
    xǁRecipeSearchIntegrationTestsǁsetUp__mutmut_orig.__name__ = 'xǁRecipeSearchIntegrationTestsǁsetUp'



    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_orig(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_1(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='XXtestuserXX', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_2(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='XXtestpassXX')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_3(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login( password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_4(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser',)
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_5(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('XXrecipe_searchXX'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_6(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'XXtermXX': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_7(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'XXsoupXX', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_8(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'XXblacklistXX': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_9(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': 'XX["Onion"]XX'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_10(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = None

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_11(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['XXrecipesXX']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_12(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()[None]
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_13(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = None
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_14(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 2)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_15(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[1]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_16(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[None]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_17(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['XXtitleXX'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_18(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0][None], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_19(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'XXTomato SoupXX')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_20(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('XXOnion SoupXX', [recipe['title'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_21(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe['XXtitleXX'] for recipe in recipes])  # Onion Soup should be excluded

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_22(self):
        # Simulate a GET request to the search view with a blacklist
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion"]'})

        # Check that recipe2 is excluded and recipe1 is included
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # Only one recipe should be returned
        self.assertEqual(recipes[0]['title'], 'Tomato Soup')  # Tomato Soup should be in the results
        self.assertNotIn('Onion Soup', [recipe[None] for recipe in recipes])  # Onion Soup should be excluded

    xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_mutants = {
    'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_1': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_1, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_2': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_2, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_3': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_3, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_4': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_4, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_5': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_5, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_6': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_6, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_7': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_7, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_8': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_8, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_9': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_9, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_10': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_10, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_11': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_11, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_12': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_12, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_13': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_13, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_14': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_14, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_15': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_15, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_16': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_16, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_17': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_17, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_18': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_18, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_19': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_19, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_20': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_20, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_21': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_21, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_22': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_22
    }

    def test_blacklisted_ingredients_exclusion(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_orig"), object.__getattribute__(self, "xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_mutants"), *args, **kwargs)
        return result 

    test_blacklisted_ingredients_exclusion.__signature__ = _mutmut_signature(xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_orig)
    xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion__mutmut_orig.__name__ = 'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_exclusion'



    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_orig(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_1(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='XXtestuserXX', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_2(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='XXtestpassXX')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_3(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login( password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_4(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser',)
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_5(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('XXrecipe_searchXX'), {'term': 'soup', 'blacklist': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_6(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'XXtermXX': 'soup', 'blacklist': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_7(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'XXsoupXX', 'blacklist': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_8(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'XXblacklistXX': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_9(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': 'XX["Onion", "Tomato"]XX'})

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_10(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = None

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_11(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = response.json()['XXrecipesXX']
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_12(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = response.json()[None]
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_13(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = None
        self.assertEqual(len(recipes), 0)  # No recipes should be returned

    def xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_14(self):
        # Simulate a GET request to the search view with a blacklist that excludes all recipes
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('recipe_search'), {'term': 'soup', 'blacklist': '["Onion", "Tomato"]'})

        # Check that no recipes are returned
        recipes = response.json()['recipes']
        self.assertEqual(len(recipes), 1)  # No recipes should be returned

    xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_mutants = {
    'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_1': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_1, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_2': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_2, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_3': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_3, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_4': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_4, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_5': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_5, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_6': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_6, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_7': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_7, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_8': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_8, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_9': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_9, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_10': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_10, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_11': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_11, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_12': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_12, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_13': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_13, 
        'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_14': xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_14
    }

    def test_blacklisted_ingredients_no_results(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_orig"), object.__getattribute__(self, "xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_mutants"), *args, **kwargs)
        return result 

    test_blacklisted_ingredients_no_results.__signature__ = _mutmut_signature(xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_orig)
    xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results__mutmut_orig.__name__ = 'xǁRecipeSearchIntegrationTestsǁtest_blacklisted_ingredients_no_results'



# Unit tests for Blacklist
class RecipeSearchUnitTests(TestCase):

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_orig(self):
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

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_1(self):
        # Create a user
        self.user = User.objects.create_user(username='XXtestuserXX', password='testpass')

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

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_2(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='XXtestpassXX')

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

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_3(self):
        # Create a user
        self.user = User.objects.create_user( password='testpass')

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

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_4(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser',)

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

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_5(self):
        # Create a user
        self.user = None

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

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_6(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='XXTomatoXX')
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

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_7(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = None
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

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_8(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='XXOnionXX')
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

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_9(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = None
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

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_10(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='XXGarlicXX')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', api_id='api_001', calories=150)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='api_002', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_11(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = None

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', api_id='api_001', calories=150)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='api_002', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_12(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='XXTomato SoupXX', api_id='api_001', calories=150)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='api_002', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_13(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', api_id='XXapi_001XX', calories=150)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='api_002', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_14(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', api_id='api_001', calories=151)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='api_002', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_15(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create( api_id='api_001', calories=150)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='api_002', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_16(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', calories=150)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='api_002', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_17(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', api_id='api_001',)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='api_002', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_18(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = None
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='api_002', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_19(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', api_id='api_001', calories=150)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='XXOnion SoupXX', api_id='api_002', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_20(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', api_id='api_001', calories=150)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='XXapi_002XX', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_21(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', api_id='api_001', calories=150)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='api_002', calories=101)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_22(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', api_id='api_001', calories=150)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create( api_id='api_002', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_23(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', api_id='api_001', calories=150)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', calories=100)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_24(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', api_id='api_001', calories=150)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = Recipe.objects.create(title='Onion Soup', api_id='api_002',)
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_25(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(name='Tomato')
        self.ingredient2 = Ingredient.objects.create(name='Onion')
        self.ingredient3 = Ingredient.objects.create(name='Garlic')

        # Create recipes
        self.recipe1 = Recipe.objects.create(title='Tomato Soup', api_id='api_001', calories=150)
        self.recipe1.ingredients.add(self.ingredient1)

        self.recipe2 = None
        self.recipe2.ingredients.add(self.ingredient2)

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_26(self):
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

        self.recipe3 = Recipe.objects.create(title='XXGarlic BreadXX', api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_27(self):
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

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='XXapi_003XX', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_28(self):
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

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003', calories=201)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_29(self):
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

        self.recipe3 = Recipe.objects.create( api_id='api_003', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_30(self):
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

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', calories=200)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_31(self):
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

        self.recipe3 = Recipe.objects.create(title='Garlic Bread', api_id='api_003',)
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_32(self):
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

        self.recipe3 = None
        self.recipe3.ingredients.add(self.ingredient3)

        # Create user preference
        self.user_pref = UserPreference.objects.create(user=self.user)

    def xǁRecipeSearchUnitTestsǁsetUp__mutmut_33(self):
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
        self.user_pref = None

    xǁRecipeSearchUnitTestsǁsetUp__mutmut_mutants = {
    'xǁRecipeSearchUnitTestsǁsetUp__mutmut_1': xǁRecipeSearchUnitTestsǁsetUp__mutmut_1, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_2': xǁRecipeSearchUnitTestsǁsetUp__mutmut_2, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_3': xǁRecipeSearchUnitTestsǁsetUp__mutmut_3, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_4': xǁRecipeSearchUnitTestsǁsetUp__mutmut_4, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_5': xǁRecipeSearchUnitTestsǁsetUp__mutmut_5, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_6': xǁRecipeSearchUnitTestsǁsetUp__mutmut_6, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_7': xǁRecipeSearchUnitTestsǁsetUp__mutmut_7, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_8': xǁRecipeSearchUnitTestsǁsetUp__mutmut_8, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_9': xǁRecipeSearchUnitTestsǁsetUp__mutmut_9, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_10': xǁRecipeSearchUnitTestsǁsetUp__mutmut_10, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_11': xǁRecipeSearchUnitTestsǁsetUp__mutmut_11, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_12': xǁRecipeSearchUnitTestsǁsetUp__mutmut_12, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_13': xǁRecipeSearchUnitTestsǁsetUp__mutmut_13, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_14': xǁRecipeSearchUnitTestsǁsetUp__mutmut_14, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_15': xǁRecipeSearchUnitTestsǁsetUp__mutmut_15, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_16': xǁRecipeSearchUnitTestsǁsetUp__mutmut_16, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_17': xǁRecipeSearchUnitTestsǁsetUp__mutmut_17, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_18': xǁRecipeSearchUnitTestsǁsetUp__mutmut_18, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_19': xǁRecipeSearchUnitTestsǁsetUp__mutmut_19, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_20': xǁRecipeSearchUnitTestsǁsetUp__mutmut_20, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_21': xǁRecipeSearchUnitTestsǁsetUp__mutmut_21, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_22': xǁRecipeSearchUnitTestsǁsetUp__mutmut_22, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_23': xǁRecipeSearchUnitTestsǁsetUp__mutmut_23, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_24': xǁRecipeSearchUnitTestsǁsetUp__mutmut_24, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_25': xǁRecipeSearchUnitTestsǁsetUp__mutmut_25, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_26': xǁRecipeSearchUnitTestsǁsetUp__mutmut_26, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_27': xǁRecipeSearchUnitTestsǁsetUp__mutmut_27, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_28': xǁRecipeSearchUnitTestsǁsetUp__mutmut_28, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_29': xǁRecipeSearchUnitTestsǁsetUp__mutmut_29, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_30': xǁRecipeSearchUnitTestsǁsetUp__mutmut_30, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_31': xǁRecipeSearchUnitTestsǁsetUp__mutmut_31, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_32': xǁRecipeSearchUnitTestsǁsetUp__mutmut_32, 
        'xǁRecipeSearchUnitTestsǁsetUp__mutmut_33': xǁRecipeSearchUnitTestsǁsetUp__mutmut_33
    }

    def setUp(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeSearchUnitTestsǁsetUp__mutmut_orig"), object.__getattribute__(self, "xǁRecipeSearchUnitTestsǁsetUp__mutmut_mutants"), *args, **kwargs)
        return result 

    setUp.__signature__ = _mutmut_signature(xǁRecipeSearchUnitTestsǁsetUp__mutmut_orig)
    xǁRecipeSearchUnitTestsǁsetUp__mutmut_orig.__name__ = 'xǁRecipeSearchUnitTestsǁsetUp'



    def xǁRecipeSearchUnitTestsǁtest_add_to_blacklist__mutmut_orig(self):
        # Add ingredient to blacklist
        self.user_pref.blacklist.add(self.ingredient1)
        self.assertIn(self.ingredient1, self.user_pref.blacklist.all())

    xǁRecipeSearchUnitTestsǁtest_add_to_blacklist__mutmut_mutants = {

    }

    def test_add_to_blacklist(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeSearchUnitTestsǁtest_add_to_blacklist__mutmut_orig"), object.__getattribute__(self, "xǁRecipeSearchUnitTestsǁtest_add_to_blacklist__mutmut_mutants"), *args, **kwargs)
        return result 

    test_add_to_blacklist.__signature__ = _mutmut_signature(xǁRecipeSearchUnitTestsǁtest_add_to_blacklist__mutmut_orig)
    xǁRecipeSearchUnitTestsǁtest_add_to_blacklist__mutmut_orig.__name__ = 'xǁRecipeSearchUnitTestsǁtest_add_to_blacklist'



    def xǁRecipeSearchUnitTestsǁtest_remove_from_blacklist__mutmut_orig(self):
        # Add and remove an ingredient from the blacklist
        self.user_pref.blacklist.add(self.ingredient1)
        self.user_pref.blacklist.remove(self.ingredient1)
        self.assertNotIn(self.ingredient1, self.user_pref.blacklist.all())

    xǁRecipeSearchUnitTestsǁtest_remove_from_blacklist__mutmut_mutants = {

    }

    def test_remove_from_blacklist(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeSearchUnitTestsǁtest_remove_from_blacklist__mutmut_orig"), object.__getattribute__(self, "xǁRecipeSearchUnitTestsǁtest_remove_from_blacklist__mutmut_mutants"), *args, **kwargs)
        return result 

    test_remove_from_blacklist.__signature__ = _mutmut_signature(xǁRecipeSearchUnitTestsǁtest_remove_from_blacklist__mutmut_orig)
    xǁRecipeSearchUnitTestsǁtest_remove_from_blacklist__mutmut_orig.__name__ = 'xǁRecipeSearchUnitTestsǁtest_remove_from_blacklist'



    def xǁRecipeSearchUnitTestsǁtest_multiple_ingredients_in_blacklist__mutmut_orig(self):
        # Add multiple ingredients to the blacklist
        self.user_pref.blacklist.add(self.ingredient1, self.ingredient2)
        self.assertIn(self.ingredient1, self.user_pref.blacklist.all())
        self.assertIn(self.ingredient2, self.user_pref.blacklist.all())

    xǁRecipeSearchUnitTestsǁtest_multiple_ingredients_in_blacklist__mutmut_mutants = {

    }

    def test_multiple_ingredients_in_blacklist(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeSearchUnitTestsǁtest_multiple_ingredients_in_blacklist__mutmut_orig"), object.__getattribute__(self, "xǁRecipeSearchUnitTestsǁtest_multiple_ingredients_in_blacklist__mutmut_mutants"), *args, **kwargs)
        return result 

    test_multiple_ingredients_in_blacklist.__signature__ = _mutmut_signature(xǁRecipeSearchUnitTestsǁtest_multiple_ingredients_in_blacklist__mutmut_orig)
    xǁRecipeSearchUnitTestsǁtest_multiple_ingredients_in_blacklist__mutmut_orig.__name__ = 'xǁRecipeSearchUnitTestsǁtest_multiple_ingredients_in_blacklist'



    def xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_orig(self):
        # Test filtering recipes based on blacklist
        blacklist = ['Onion']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2, filtered_recipes)
        self.assertIn(self.recipe1, filtered_recipes)
        self.assertIn(self.recipe3, filtered_recipes)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_1(self):
        # Test filtering recipes based on blacklist
        blacklist = ['XXOnionXX']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2, filtered_recipes)
        self.assertIn(self.recipe1, filtered_recipes)
        self.assertIn(self.recipe3, filtered_recipes)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_2(self):
        # Test filtering recipes based on blacklist
        blacklist = None

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2, filtered_recipes)
        self.assertIn(self.recipe1, filtered_recipes)
        self.assertIn(self.recipe3, filtered_recipes)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_3(self):
        # Test filtering recipes based on blacklist
        blacklist = ['Onion']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=None)

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2, filtered_recipes)
        self.assertIn(self.recipe1, filtered_recipes)
        self.assertIn(self.recipe3, filtered_recipes)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_4(self):
        # Test filtering recipes based on blacklist
        blacklist = ['Onion']

        # Simulate blacklist filtering logic
        filtered_recipes = None

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2, filtered_recipes)
        self.assertIn(self.recipe1, filtered_recipes)
        self.assertIn(self.recipe3, filtered_recipes)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_5(self):
        # Test filtering recipes based on blacklist
        blacklist = ['Onion']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2, None)
        self.assertIn(self.recipe1, filtered_recipes)
        self.assertIn(self.recipe3, filtered_recipes)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_6(self):
        # Test filtering recipes based on blacklist
        blacklist = ['Onion']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2,)
        self.assertIn(self.recipe1, filtered_recipes)
        self.assertIn(self.recipe3, filtered_recipes)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_7(self):
        # Test filtering recipes based on blacklist
        blacklist = ['Onion']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2, filtered_recipes)
        self.assertIn(self.recipe1, None)
        self.assertIn(self.recipe3, filtered_recipes)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_8(self):
        # Test filtering recipes based on blacklist
        blacklist = ['Onion']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2, filtered_recipes)
        self.assertIn(self.recipe1,)
        self.assertIn(self.recipe3, filtered_recipes)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_9(self):
        # Test filtering recipes based on blacklist
        blacklist = ['Onion']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2, filtered_recipes)
        self.assertIn(self.recipe1, filtered_recipes)
        self.assertIn(self.recipe3, None)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_10(self):
        # Test filtering recipes based on blacklist
        blacklist = ['Onion']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that 'Onion Soup' is filtered out
        self.assertNotIn(self.recipe2, filtered_recipes)
        self.assertIn(self.recipe1, filtered_recipes)
        self.assertIn(self.recipe3,)

    xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_mutants = {
    'xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_1': xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_1, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_2': xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_2, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_3': xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_3, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_4': xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_4, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_5': xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_5, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_6': xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_6, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_7': xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_7, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_8': xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_8, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_9': xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_9, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_10': xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_10
    }

    def test_blacklist_filtering(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_orig"), object.__getattribute__(self, "xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_mutants"), *args, **kwargs)
        return result 

    test_blacklist_filtering.__signature__ = _mutmut_signature(xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_orig)
    xǁRecipeSearchUnitTestsǁtest_blacklist_filtering__mutmut_orig.__name__ = 'xǁRecipeSearchUnitTestsǁtest_blacklist_filtering'



    def xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_orig(self):
        # Test with blacklist that excludes all recipes
        blacklist = ['Onion', 'Tomato', 'Garlic']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that no recipes are returned
        self.assertEqual(filtered_recipes.count(), 0)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_1(self):
        # Test with blacklist that excludes all recipes
        blacklist = ['XXOnionXX', 'Tomato', 'Garlic']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that no recipes are returned
        self.assertEqual(filtered_recipes.count(), 0)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_2(self):
        # Test with blacklist that excludes all recipes
        blacklist = ['Onion', 'XXTomatoXX', 'Garlic']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that no recipes are returned
        self.assertEqual(filtered_recipes.count(), 0)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_3(self):
        # Test with blacklist that excludes all recipes
        blacklist = ['Onion', 'Tomato', 'XXGarlicXX']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that no recipes are returned
        self.assertEqual(filtered_recipes.count(), 0)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_4(self):
        # Test with blacklist that excludes all recipes
        blacklist = None

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that no recipes are returned
        self.assertEqual(filtered_recipes.count(), 0)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_5(self):
        # Test with blacklist that excludes all recipes
        blacklist = ['Onion', 'Tomato', 'Garlic']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=None)

        # Check that no recipes are returned
        self.assertEqual(filtered_recipes.count(), 0)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_6(self):
        # Test with blacklist that excludes all recipes
        blacklist = ['Onion', 'Tomato', 'Garlic']

        # Simulate blacklist filtering logic
        filtered_recipes = None

        # Check that no recipes are returned
        self.assertEqual(filtered_recipes.count(), 0)

    def xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_7(self):
        # Test with blacklist that excludes all recipes
        blacklist = ['Onion', 'Tomato', 'Garlic']

        # Simulate blacklist filtering logic
        filtered_recipes = Recipe.objects.exclude(ingredients__name__in=blacklist)

        # Check that no recipes are returned
        self.assertEqual(filtered_recipes.count(), 1)

    xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_mutants = {
    'xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_1': xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_1, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_2': xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_2, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_3': xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_3, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_4': xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_4, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_5': xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_5, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_6': xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_6, 
        'xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_7': xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_7
    }

    def test_blacklist_with_no_results(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_orig"), object.__getattribute__(self, "xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_mutants"), *args, **kwargs)
        return result 

    test_blacklist_with_no_results.__signature__ = _mutmut_signature(xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_orig)
    xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results__mutmut_orig.__name__ = 'xǁRecipeSearchUnitTestsǁtest_blacklist_with_no_results'



        
