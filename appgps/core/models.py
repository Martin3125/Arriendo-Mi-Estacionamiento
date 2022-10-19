from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=16, null=False)
    apellido = models.CharField( max_length=16, null=False)
    email = models.EmailField(primary_key=True, unique=True)
    pwd = models.CharField(null=False, max_length=12)