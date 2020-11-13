from django.db import models

# Create your models here.
class Region(models.Model):
    nombre = models.CharField(max_length=40)
    activo = models.BooleanField(default=True)

class Asesor(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=20)
    documento = models.CharField(max_length=11)
    telefono = models.CharField(max_length=9)
    correo = models.CharField(max_length=50, null=True)
    funcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=19, decimal_places=10)
    foto = models.ImageField(blank=True, upload_to='asesor/')
    region = models.ForeignKey(Region, on_delete=models.PROTECT)