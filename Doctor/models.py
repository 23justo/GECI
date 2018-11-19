from django.db import models

# Create your models here.
class Doctor(models.Model):
    nombres = models.CharField(max_length = 75)
    apellidos = models.CharField(max_length = 150)
    telefono = models.CharField(max_length = 25)
    fecha_nacimiento = models.DateField()
    clinica = models.ForeignKey(to='Clinica.Clinica')
    sexo = models.CharField(max_length=20,choices=(('Masculino','Masculino'),('Femenino','Femenino')))
    especialidad = models.CharField(max_length = 75)
    direccion_clinica = models.CharField(max_length = 150)
    dpi = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.nombres + ", "+self.apellidos

    