from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Marcas (models.Model):
    name = models.CharField(max_length=100)
    contacto_name = models.CharField(max_length=100)
    contacto_mail = models.EmailField()
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    activo = models.BooleanField(default=True)

class Ropa (models.Model):
    ropa_name = models.CharField(max_length=200)
    ropa_color = models.CharField(max_length=100)
    ropa_marca = models.CharField(max_length=100)
    ropa_precio = models.FloatField()
    ropa_imagen = models.ImageField(upload_to="ropa", null=True)

class Championes (models.Model):
    championes_name = models.CharField(max_length=200)
    championes_color = models.CharField(max_length=100)
    championes_marca = models.CharField(max_length=100)
    championes_precio = models.FloatField()
    championes_imagen = models.ImageField(upload_to="championes", null=True)

class Accesorios (models.Model):
    accesorio_name = models.CharField(max_length=200) 
    accesorio_tipo = models.CharField(max_length=100)
    accesorio_marca = models.CharField(max_length=100)
    accesorio_precio = models.FloatField()
    accesorio_imagen = models.ImageField(upload_to="accesorios", null=True)