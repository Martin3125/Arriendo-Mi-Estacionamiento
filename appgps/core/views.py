from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render  
from .models import *

# Create your views here.

#renderiza el home de la pagina.
def home(request):
    return render(request, 'core/home.html')

#inicio de sesion del usuario registrado
def login(request):
    if request.method == 'POST':
        try:
            newUser = Usuario.objects.get(email = request.POST['email'], pwd = request.POST['password'])
            request.session['email'] = newUser.email
            return redirect('home')
        except Usuario.DoesNotExist as e: 
            messages.success(request, 'Correo o constraseña no son correctos')
    return render(request, 'core/login.html')

#registra y valida un nuevo usuario
def registro(request):
    if request.method == 'POST':
        #estructura de condicion que verifica si el usuario que se intenta registrar existe
        if Usuario.objects.filter(email = request.POST['email']).exists(): # se verifica la existencia por el campo de email
            messages.success(request, 'El usuario ingresado ya existe')
        else:
            #creacion del nuevo usuario, entre [] se coloca el atributo "name" de los input en el html
            newUser = Usuario(
                nombre = request.POST['nombre'],
                apellido = request.POST['apellido'],
                email = request.POST['email'],
                pwd = request.POST['password'],
                tipo_usuario = False
            )
            newUser.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('login')
    return render(request, 'core/registro.html')

#renderiza a la pagina donde se registra un nuevo estacionamiento.
def arriendo(request):
    return render(request, 'core/arriendo.html')
    
#renderiza a la pagina donde se encuntran las funciones de ajustes.
def ajustes(request):
    return render(request, 'core/ajustes.html')

#renderiza a la pagina donde se encuentyra el crud de usuarios.
def paginaCuenta(request):
    return render(request, 'core/eliminarCuenta.html')

#Elimina la cuenta de un usuario por el id (funcion de admin).
def eliminarCuenta(request, email):
    usuarios = Usuario.objects.get(email=email)
    usuarios.delete()
    return redirect('login')

#Trae la informacion del usuario con la sesion activa 
def perfil(request):
    usuario = Usuario.objects.filter(email = request.session['email'])
    return render(request, 'core/perfil.html', {'usuario':usuario})

#renderiza a la pagina para actualizar los datos del usuario.
def actualizarPerfil(request, email):
    usuario = Usuario.objects.get(email = email)
    return render(request, 'core/editarPerfil.html', {'usuario':usuario})

#edita el perfil del usuario de la sesion activa.
def editarPerfil(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']

    oldemail = Usuario.objects.get(email = request.session['email'])  
    oldemail.nombre = nombre
    oldemail.apellido = apellido
    oldemail.save()
    messages.success(request, 'Usuario: ' + nombre +' Actualizado correctamente!')
    return redirect('perfil')

#llama a todos los objetos de la tabla usuario.
def crudUsuario(request):
    contexto = {'usuario': Usuario.objects.all()}
    return render(request, 'core/crudUsuario.html', contexto)

# elimina al usario por el id (funcion de admin).
def eliminarUsuario(request, email):
    usuario = Usuario.objects.get(email=email)
    usuario.delete()
    return redirect('crudUsuario')

#llama a todos los objetos de la tabla ubicacion.
def crudUbicaciones(request):
    contexto = {'ubicacion': Ubicacion.objects.all()}
    return render(request, 'core/crudUbicaciones.html', contexto)

#elimina la ubicacion por su id (funcion de admin).
def eliminarUbicacion(request, nombre):
    ubicacion = Ubicacion.objects.get(nombre=nombre)
    ubicacion.delete()
    return redirect('crudUbicaciones')

# elimina la sesion iniciada.
def cerrarSesion(request):
    del request.session['email']
    request.session.modified = True
    messages.success(request, 'Sesion Cerrada')
    return render(request, 'core/ajustes.html')

#guarda la ubicacion del estacionamiento con la fecha en tiepo real.
def addUbicacion(request):
    nombre = request.POST['nombre']
    lat = request.POST['lat']
    lng = request.POST['lng']
    precio = request.POST['precio']
    usuario= request.session['email']
    fecha = datetime.now()
    newUbicacion = Ubicacion(nombre =nombre, lat = lat, lng = lng,precio = precio,user = usuario, fecha = fecha)
    newUbicacion.save()
    print('funca')
    return redirect('home')


# obtiene todos los datos de las ubicaciones y les da formato JSON
def obtener(request):
    ubicaciones = list(Ubicacion.objects.values())
    if (len(ubicaciones) > 0):
        data = {'message': "Success", 'ubicaciones': ubicaciones}
    else:
        data = {'message': "Not Found"}

    return JsonResponse(data)

#carga la pagina arriendo estacionamiento obteniendo la ubicacion por su id.
def arriendoEs(request, nombre):
    ubicacion = Ubicacion.objects.get(nombre=nombre)
    return render(request, 'core/arriendoEs.html', {'ubicacion':ubicacion})

#Guarda el arriendo elegido.
def confirmarArriendo(request, nombre):
    nombre = request.POST['nombre']
    lat = request.POST['lat']
    lng = request.POST['lng']   
    precio = request.POST['precio']
    dueño = request.POST['dueño']
    fecha = request.POST['fecha']
    user= request.session['email']
    newArriendoEs = ArriendoEs(user = user, nombreEs =nombre, lat = lat, lng = lng,precio = precio,dueño = dueño, fecha = fecha)
    newArriendoEs.save()

    oldUbicacion = Ubicacion.objects.get(nombre=nombre)
    oldUbicacion.delete()

    return redirect('home')