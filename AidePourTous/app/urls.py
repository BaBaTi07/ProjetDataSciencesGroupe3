from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path('category/<str:category>/', views.category_view, name='category'),
]