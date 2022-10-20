from django import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('registro', registro, name='registro'),
    path('arriendo', arriendo, name='arriendo'),
    path('ajustes', ajustes, name='ajustes'),
    path('perfil', perfil, name='perfil'),
    path('editarPerfil', editarPerfil, name="editarPerfil"),
    #funciones del crud
    path('crudUsuario', crudUsuario, name='crudUsuario'),
    path('eliminarUsuario/<email>', eliminarUsuario, name='eliminarUsuario'),
]