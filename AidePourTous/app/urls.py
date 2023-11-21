from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path('menu1/',views.menu1, name='menu1'),
    path('menu2/', views.menu2, name='menu2'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
]