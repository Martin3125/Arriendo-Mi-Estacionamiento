from datetime import datetime, date
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
def calcularArriendo(request, nombre):
    nombre = request.POST['nombreEs']
    lat = request.POST['lat']
    lng = request.POST['lng']   
    precio = request.POST['precio']
    dueño = request.POST['dueño']
    fecha = request.POST['fecha']
    user= request.session['email']
    h_inicio = int(request.POST['h_inicio'])
    h_salida = int(request.POST['h_salida'])
    print(type(h_inicio))
    print(type(h_salida))
    total_pagar = precio*(h_salida - h_inicio)
    
    newArriendoEs = ArriendoEs(user = user, nombreEs =nombre, lat = lat, lng = lng,precio = precio,dueño = dueño, fecha = fecha, h_inicio = h_inicio, h_salida = h_salida, totalPago = total_pagar)
    print("funca")
    print(total_pagar)
    newArriendoEs.save()

    contexto ={'ubicacion': Ubicacion.objects.get(nombre=nombre)}
    return render(request, 'core/arriendoEs.html', contexto)

#Guarda el arriendo elegido.

def confirmarArriendo(request, nombre):
    nombreEs = request.POST['nombreEs'] 
    lat = request.POST['lat']
    lng = request.POST['lng']
    precio = int(request.POST['precio'])
    dueño = request.POST['dueño']
    fecha = request.POST['fecha']
    user= request.session['email']
    h_inicio = int(request.POST['h_inicio'])
    h_salida = int(request.POST['h_salida'])
    rut = request.POST['rut']
    patente = request.POST['patente']
    print(type(h_inicio))
    print(type(h_salida))
    total_pagar = precio*(h_salida - h_inicio)
    
    newArriendoEs = ArriendoEs(user = user, nombreEs = nombreEs, lat = lat, lng = lng, precio = precio, dueño = dueño, fecha = fecha, h_inicio = h_inicio, h_salida = h_salida, totalPago = total_pagar)
    newUser = Usuario.objects.get(email = user)
    newUser.rut = rut
    newUser.patente = patente
    print("funca")
    print(total_pagar)
    newUser.save()
    newArriendoEs.save()

    oldUbicacion = Ubicacion.objects.get(nombre=nombre)
    oldUbicacion.disponible = False
    oldUbicacion.save()
    return redirect('home')



def misArriendos(request ):
    contexto = {'ubicacion': Ubicacion.objects.obtener_user(user= request.session['email'])}
    # disponible = request.POST['a']
    # print(disponible)
    return render(request, 'core/misArriendos.html', contexto)

def ValidacionDatos(request):
    return render(request, 'core/ValidacionDatos.html')

def Pagos(request):
    contexto1 = {'user' :ArriendoEs.objects.get(user = request.session['email'])}
    return render(request, 'core/Pagos.html',contexto1)

def Pagos1(request):
    contexto2 = {'cuenta': Cuenta.objects.get(user = request.session['email'])}
    return render(request, 'core/Pagos.html',contexto2)
    
def Disponible(request,nombre):
    ubicacion = Ubicacion.objects.get(nombre =nombre)
    if ubicacion.disponible == True:
        ubicacion.disponible = False
    else:
        ubicacion.disponible = True
    ubicacion.save()
    print(ubicacion) 
    contexto = {'ubicacion': Ubicacion.objects.obtener_user(user= request.session['email'])}
    return render(request, 'core/misArriendos.html',contexto)


def ValidacionCuenta(request):
    user = request.session['email']
    nombre = request.POST['nombre']
    nombreBanco = request.POST['nombreBanco']
    numTarjeta = request.POST['numTarjeta']
    MM = request.POST['MM']
    YY = request.POST['YY']
    CCV = request.POST['CCV']
    newcuenta = Cuenta( user = user, nombre = nombre, nombreBanco = nombreBanco, numTarjeta = numTarjeta, MM = MM , YY = YY, CCV = CCV)
    newcuenta.save()
    print('funca')
    return redirect('ajustes')

def finalizar(request):
    id_pago = len(request.POST['nombreEs']) *99/234
    user = request.session['email']
    nombreEs = request.POST['nombreEs'] 
    h_inicio = request.POST['h_inicio']
    fecha_Pago = datetime.now()
    totalPago = request.POST['totalPago']

    newPago = Pago(id_pago = id_pago, user = user, nombreEs = nombreEs, h_inicio = h_inicio, fecha_Pago = fecha_Pago, totalPago = totalPago)
    newPago.save()

    
    oldUbicacion = Ubicacion.objects.get(nombre=nombreEs)
    oldUbicacion.disponible = True
    oldUbicacion.save()

    return redirect('home')