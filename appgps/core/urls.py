from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('registro', registro, name='registro'),
    path('arriendo', arriendo, name='arriendo'),
    path('ajustes', ajustes, name='ajustes'),
]