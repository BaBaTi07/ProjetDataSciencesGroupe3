from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def index(request):
    return HttpResponse("You're at the index page.")

def menu1(request):
    return HttpResponse("You're at the menu1 page.")

def menu2(request):
    return HttpResponse("You're at the menu2 page.")

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    return render(request, 'registration/register.html')