
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


from django.core.management.base import BaseCommand
from cookapp.models import Recipe, Ingredient, RecipeIngredient

class Command(BaseCommand):
    help = 'Clears the database of all recipes, ingredients, and recipe-ingredient relationships'

    def xǁCommandǁhandle__mutmut_orig(self, *args, **options):
        RecipeIngredient.objects.all().delete()
        Recipe.objects.all().delete()
        Ingredient.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared the database.'))

    def xǁCommandǁhandle__mutmut_1(self, *args, **options):
        RecipeIngredient.objects.all().delete()
        Recipe.objects.all().delete()
        Ingredient.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('XXSuccessfully cleared the database.XX'))

    xǁCommandǁhandle__mutmut_mutants = {
    'xǁCommandǁhandle__mutmut_1': xǁCommandǁhandle__mutmut_1
    }

    def handle(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCommandǁhandle__mutmut_orig"), object.__getattribute__(self, "xǁCommandǁhandle__mutmut_mutants"), *args, **kwargs)
        return result 

    handle.__signature__ = _mutmut_signature(xǁCommandǁhandle__mutmut_orig)
    xǁCommandǁhandle__mutmut_orig.__name__ = 'xǁCommandǁhandle'


