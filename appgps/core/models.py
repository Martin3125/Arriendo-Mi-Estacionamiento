from email.policy import default
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

class Ubicacion (models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    fecha = models.DateTimeField( auto_now_add=True)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre

class UbicacionForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Ubicacion





