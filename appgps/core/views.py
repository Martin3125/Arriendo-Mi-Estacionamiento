from datetime import datetime
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def login(request):
    if request.method == 'POST':
        try:
            newUser = Usuario.objects.get(email = request.POST['email'], pwd = request.POST['password'])
            request.session['email'] = newUser.email 
            return redirect('home')
        except Usuario.DoesNotExist as e:
            messages.success(request, 'Correo o constraseña no son correctos')
    return render(request, 'core/login.html')

def registro(request):
    if request.method == 'POST':
        #estructura de condicion que verifica si el usuario que se intenta registrar existe
        if Usuario.objects.filter(email = request.POST['correo']).exists(): # se verifica la existencia por el campo de email
            messages.success(request, 'El usuario ingresado ya existe')
        else:
            #creacion del nuevo usuario, entre [] se coloca el atributo "name" de los input en el html
            newUser = Usuario(
                nombre = request.POST['nombre'],
                apellido = request.POST['apellido'],
                email = request.POST['correo'],
                pwd = request.POST['password']
            )
            newUser.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('login')
    return render(request, 'core/registro.html')

def arriendo(request):
    return render(request, 'core/arriendo.html')

def ajustes(request):
    return render(request, 'core/ajustes.html')