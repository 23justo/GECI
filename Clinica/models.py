from django.db import models

# Create your models here.
class Clinica(models.Model):
    nombre = models.CharField(max_length = 75)
    direccion = models.CharField(max_length = 150)
    telefono = models.CharField(max_length = 25)
    moneda = models.CharField(max_length = 20, default = 'GTQ')
    color_menu = models.CharField(max_length = 50, null = True, default = '#1f262d')
    color_footer = models.CharField(max_length = 50, null = True, default = '#5c5c61')
    color_texto_menu = models.CharField(max_length = 50, null = True, default = 'white')
    def __str__(self):
        return self.nombre
