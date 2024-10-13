from django.shortcuts import render, redirect
from .models import Ingredient, Recipe, UserPreference
from .decorators import unauthenticated_user
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'cookapp/index.html')

def logout_message(request):
    return render(request, 'registration/logout.html')

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            user.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'registration/register.html', context)