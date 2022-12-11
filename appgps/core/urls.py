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
    
    
    
    
    path('cerrarSesion', cerrarSesion, name="cerrarSesion"),
    path('addUbicacion/', addUbicacion, name = "addUbicacion"),
    path('obtener', obtener, name="obtener"),

    #funciones del crud Usuario
    path('crudUsuario', crudUsuario, name='crudUsuario'),
    path('eliminarUsuario/<email>', eliminarUsuario, name='eliminarUsuario'),

    #funciones del crud Ubicacion
    path('crudUbicaciones', crudUbicaciones, name='crudUbicaciones'),
    path('eliminarUbicacion/<nombre>', eliminarUbicacion, name='eliminarUbicacion'),
    
     #funciones del crud Perfil
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    path('actualizarPerfil/<email>', actualizarPerfil, name='actualizarPerfil'),
    path('perfil', perfil, name='perfil'),

    #funciones del crud misArriendos
    path('misArriendos/', misArriendos, name='misArriendos'),
    path('disponible/<nombre>', Disponible, name='disponible'),

    

    #funciones de  ValidacionDatos
    path('ValidacionDatos', ValidacionDatos, name='ValidacionDatos'),
  
    #funciones de  Pagos
    path('Pagos', Pagos, name='Pagos'),


    # #
    # path('arrendar/<nombre>',arrendar   , name="arrendar"),
    path('arriendoEs/<nombre>',arriendoEs, name="arriendoEs"),
    path('confirmarArriendo/<nombre>',confirmarArriendo, name="confirmarArriendo"),
    

    
]
