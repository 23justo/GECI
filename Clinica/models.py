from django.db import models

# Create your models here.
class Clinica(models.Model):
    nombre = models.CharField(max_length = 75)
    direccion = models.CharField(max_length = 150)
    telefono = models.CharField(max_length = 25)
    def __str__(self):
        return self.nombre
