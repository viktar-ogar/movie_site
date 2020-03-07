from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register_page"),
    path('', views.loginPage, name="login_page"),
]