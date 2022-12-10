from multiprocessing.dummy import Value
from django.db import models
from django.forms import ModelForm


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=16, )
    apellido = models.CharField( max_length=16, null=False)
    email = models.EmailField(primary_key=True, unique=True)
    pwd = models.CharField(null=False, max_length=12)
    tipo_usuario = models.BooleanField( max_length=16, default=False)

class UbicacionManeger(models.Manager):
    def obtener_user(self, user):
        return self.filter(user=user)

    def disponible(self, disponible):
        return self.filter(disponible=disponible)    

class Ubicacion (models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)
    lat = models.FloatField(default= 0)
    lng = models.FloatField(default= 0)
    fecha = models.DateTimeField( auto_now_add=True)
    precio = models.IntegerField( default= 0)
    user = models.EmailField(max_length=50)
    disponible = models.BooleanField(default= True)

    objects = UbicacionManeger()

    def __unicode__(self):
        return self.nombre

class ArriendoEs(models.Model):
    user = models.EmailField(primary_key=True, max_length=50)
    nombreEs = models.CharField( max_length=50, null=False,default= '')
    lat = models.FloatField(default= 0)
    lng = models.FloatField(default= 0)
    precio = models.IntegerField( default= 0)
    dueño = models.EmailField(max_length=50)
    fecha = models.CharField(max_length=50)
