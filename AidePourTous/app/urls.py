from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('finance/', views.finance_view, name='finance'),
    path('housing', views.housing_view, name='housing'),
    path('food', views.food_view, name='food'),
    path('work_training', views.work_training_view, name='work_training'),
    path('chatBot', views.chatBot, name='chatBot'),
]