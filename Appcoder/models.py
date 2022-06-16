from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField("Nombre", max_length=30)
    apellido = models.CharField("Apellido", max_length=30)
    edad = models.IntegerField("Edad")
    fecha_nacimiento = models.DateField("Fecha de nacimiento")
