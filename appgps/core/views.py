from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render
    # from django.utils import json as simplejson
    # from django.http import HttpResponse
    # from django.shortcuts import render_to_response
    # from django.template import RequestContext
    # from django.utils.timesince import timesince
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


def arriendo(request):
    return render(request, 'core/arriendo.html')

def ajustes(request):
    return render(request, 'core/ajustes.html')

def paginaCuenta(request):
    return render(request, 'core/eliminarCuenta.html')
    
def eliminarCuenta(request, email):
    usuarios = Usuario.objects.get(email=email)
    usuarios.delete()
    return redirect('login')
    
def perfil(request):
    usuario = Usuario.objects.filter(email = request.session['email'])
    return render(request, 'core/perfil.html', {'usuario':usuario})

def actualizarPerfil(request, email):
    usuario = Usuario.objects.get(email = email)
    return render(request, 'core/editarPerfil.html', {'usuario':usuario})


# promo = Promo.objects.filter(id_promo = code)
#     if request.method == 'POST':
#         oldPromo = Promo.objects.get(id_promo = code)
#         if request.POST['newdesc'] != '':
#             oldPromo.descripcion = request.POST['newdesc']
#             oldPromo.save()
#         return redirect('crudPromos')
#     else:        
#         return render(request, 'app/editarPromo.html', {"promo":promo})  

def editarPerfil(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']

    oldemail = Usuario.objects.get(email = request.session['email'])  
    oldemail.nombre = nombre
    oldemail.apellido = apellido
    oldemail.save()
    messages.success(request, 'Usuario: ' + nombre +' Actualizado correctamente!')
    return redirect('perfil')
    # else:        
    #     return render(request, 'core/editarPerfil.html', {"email":email})


def crudUsuario(request):
    contexto = {'usuario': Usuario.objects.all()}
    return render(request, 'core/crudUsuario.html', contexto)


def eliminarUsuario(request, email):
    usuario = Usuario.objects.get(email=email)
    usuario.delete()
    return redirect('crudUsuario')

def crudUbicaciones(request):
    contexto = {'ubicacion': Ubicacion.objects.all()}
    return render(request, 'core/crudUbicaciones.html', contexto)


def eliminarUbicacion(request, nombre):
    usuario = Ubicacion.objects.get(nombre=nombre)
    usuario.delete()
    return redirect('crudUbicaciones')


def cerrarSesion(request):
    del request.session['email']
    request.session.modified = True
    messages.success(request, 'Sesion Cerrada')
    return render(request, 'core/ajustes.html')

# def arrendar(request):
#     form = UbicacionForm()
#     Ubicaciones = Ubicacion.objects.all().order_by('-fecha')
#     return render_to_response('arriendo.html', {'form': form}, context_instance=RequestContext(request))

# def coords_save(request):
#     if request.is_ajax():
#         form = UbicacionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             Ubicaciones = Ubicacion.objects.all().order_by('-fecha')
#             data ='<ul>'
#             for ubicacion in Ubicaciones:
#                 data += '<li>%s %s -hace %s<li>' %(ubicacion.nombre, ubicacion.user, timesince(ubicacion.fecha))
#             data +='<ul>'
#             return HttpResponse(simplejson.dumps({'ok' :True, 'msg':data }), mimetype='application/json')
#         else:
#             return HttpResponse(simplejson.dumps({'ok' :False, 'msg': 'Debes llenar todos los campos'}), mimetype='application/json')


# def arriendo(request):
#     if request.method == 'POST':
#             #creacion del nuevo usuario, entre [] se coloca el atributo "name" de los input en el html
#             newUB = Ubicacion(
#                 nombre = request.POST['nombre'],
#                 lat =request.POST['lat'],
#                 lng = request.POST['lng'],
#                 precio = request.POST['precio'],
#             )

            
#             newUB.save()
#             messages.success(request, 'Usuario registrado correctamente')
#             return redirect('home')
#     return render(request, 'core/arriendo.html')


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


def obtener(request):
    ubicaciones = list(Ubicacion.objects.values())
    if (len(ubicaciones) > 0):
        data = {'message': "Success", 'ubicaciones': ubicaciones}
    else:
        data = {'message': "Not Found"}

    return JsonResponse(data)