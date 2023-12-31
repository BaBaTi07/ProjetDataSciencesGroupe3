from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Etablissement, Message
from .forms import MessageForm
from .chatBot import get_response

def home(request):
    return render(request, 'home.html')

@login_required
def advise(request):
    return render(request, 'advise.html')

@login_required
def finance_view(request):
    return render(request, 'category/finance.html')

@login_required
def housing_view(request):
    # Fetch the housing data from the database
    housing_data = Etablissement.objects.all().values()

    # Pass the data to the template
    context = {'housing_data': list(housing_data)}
    
    return render(request,'category/housing.html',context)

@login_required
def food_view(request):
    return render(request, 'category/food.html')

@login_required
def work_training_view(request):
    return render(request, 'category/work_training.html')

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
            return redirect('chatBot')  # Redirect to the chatbot page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout

@login_required
def profile_view(request):
    # Ajoutez ici la logique pour récupérer les informations du profil de l'utilisateur
    # Par exemple, vous pouvez utiliser request.user pour accéder à l'utilisateur actuel
    user_info = {
        'username': request.user.username,
        'email': request.user.email,
        # Ajoutez d'autres informations du profil ici
    }

    return render(request, 'profile.html', {'user_info': user_info})

@login_required
def chatBot(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                text=form.cleaned_data['message'],
                user = request.user,
                bot = False)
            
            return redirect('reponse', message=form.cleaned_data['message'])
    else:
        form = MessageForm()

    messages = Message.objects.filter(user = request.user).order_by('created_at')
    return render(request, 'chatBot.html', {'messages': messages, 'form': form})

@login_required
def clear_messages(request):
    if request.method == 'POST':
        Message.objects.filter(user = request.user).delete()
        return redirect('chatBot') 

@login_required
def reponse(request, message):
    reponse = get_response(message)
    print (reponse.content)
    Message.objects.create(
        text = reponse.content,
        user = request.user,
        bot = True)
    return redirect('chatBot')