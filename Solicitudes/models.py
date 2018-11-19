from django.db import models

# Create your models here.
class Solicitudes(models.Model):
    correo = models.EmailField()
    nombre_completo = models.CharField(max_length=250)
    tema = models.CharField(max_length=250)
    mensaje = models.TextField()
