
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


from django.http import HttpResponse
from django.shortcuts import redirect

def x_unauthenticated_user__mutmut_orig(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def x_unauthenticated_user__mutmut_1(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('XXindexXX')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def x_unauthenticated_user__mutmut_2(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(None, *args, **kwargs)
    
    return wrapper_func

def x_unauthenticated_user__mutmut_3(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func( *args, **kwargs)
    
    return wrapper_func

def x_unauthenticated_user__mutmut_4(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, **kwargs)
    
    return wrapper_func

def x_unauthenticated_user__mutmut_5(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args,)
    
    return wrapper_func

x_unauthenticated_user__mutmut_mutants = {
'x_unauthenticated_user__mutmut_1': x_unauthenticated_user__mutmut_1, 
    'x_unauthenticated_user__mutmut_2': x_unauthenticated_user__mutmut_2, 
    'x_unauthenticated_user__mutmut_3': x_unauthenticated_user__mutmut_3, 
    'x_unauthenticated_user__mutmut_4': x_unauthenticated_user__mutmut_4, 
    'x_unauthenticated_user__mutmut_5': x_unauthenticated_user__mutmut_5
}

def unauthenticated_user(*args, **kwargs):
    result = _mutmut_trampoline(x_unauthenticated_user__mutmut_orig, x_unauthenticated_user__mutmut_mutants, *args, **kwargs)
    return result 

unauthenticated_user.__signature__ = _mutmut_signature(x_unauthenticated_user__mutmut_orig)
x_unauthenticated_user__mutmut_orig.__name__ = 'x_unauthenticated_user'



def x_allowed_users__mutmut_orig(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator

def x_allowed_users__mutmut_1(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = ""
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator

def x_allowed_users__mutmut_2(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[1].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator

def x_allowed_users__mutmut_3(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[None].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator

def x_allowed_users__mutmut_4(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = None

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator

def x_allowed_users__mutmut_5(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group not in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator

def x_allowed_users__mutmut_6(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(None, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator

def x_allowed_users__mutmut_7(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func( *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator

def x_allowed_users__mutmut_8(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator

def x_allowed_users__mutmut_9(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args,)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator

def x_allowed_users__mutmut_10(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('XXYou are not authorized to view this page.XX')
        return wrapper_func
    return decorator

x_allowed_users__mutmut_mutants = {
'x_allowed_users__mutmut_1': x_allowed_users__mutmut_1, 
    'x_allowed_users__mutmut_2': x_allowed_users__mutmut_2, 
    'x_allowed_users__mutmut_3': x_allowed_users__mutmut_3, 
    'x_allowed_users__mutmut_4': x_allowed_users__mutmut_4, 
    'x_allowed_users__mutmut_5': x_allowed_users__mutmut_5, 
    'x_allowed_users__mutmut_6': x_allowed_users__mutmut_6, 
    'x_allowed_users__mutmut_7': x_allowed_users__mutmut_7, 
    'x_allowed_users__mutmut_8': x_allowed_users__mutmut_8, 
    'x_allowed_users__mutmut_9': x_allowed_users__mutmut_9, 
    'x_allowed_users__mutmut_10': x_allowed_users__mutmut_10
}

def allowed_users(*args, **kwargs):
    result = _mutmut_trampoline(x_allowed_users__mutmut_orig, x_allowed_users__mutmut_mutants, *args, **kwargs)
    return result 

allowed_users.__signature__ = _mutmut_signature(x_allowed_users__mutmut_orig)
x_allowed_users__mutmut_orig.__name__ = 'x_allowed_users'


