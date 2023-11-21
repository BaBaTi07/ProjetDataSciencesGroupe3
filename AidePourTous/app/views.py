from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def category_view(request, category):
    # Add logic to fetch and display content based on the category
    return render(request, 'category.html', {'category': category})

def index(request):
    return HttpResponse("You're at the index page.")

def menu1(request):
    return HttpResponse("You're at the menu1 page.")

def menu2(request):
    return HttpResponse("You're at the menu2 page.")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})