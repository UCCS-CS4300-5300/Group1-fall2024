from django.shortcuts import render, redirect
from .models import Ingredient, Recipe, UserPreference
from .decorators import unauthenticated_user
from .forms import CreateUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'cookapp/index.html')

def logout_message(request):
    return render(request, 'registration/logout.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().username}!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            user.save()

            messages.success(request, f'Welcome, {username}!')
            print(f'Messages: {messages.get_messages(request)}')  # Debugging line
            return redirect('index')  # Redirect to the home page
    context = {'form': form}
    return render(request, 'registration/register.html', context)