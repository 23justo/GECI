from django.db import models
import datetime

# Create your models here.
class Paciente(models.Model):
    tipos_de_sangre = (
        ('A Positiva','A Positiva'),
        ('A Negativo','A Negativo'),
        ('B Positivo','B Positivo'),
        ('B Negativo','B Negativo'),
        ('O Positivo','O Positivo'),
        ('AB Positivo','AB Positivo'),
        ('AB Negativo','AB Negativo'),
    )
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    sexo = models.CharField(max_length=20,choices=(('Masculino','Masculino'),('Femenino','Femenino')))
    fecha_nacimiento = models.DateField()
    tipo_sangre = models.CharField(choices=tipos_de_sangre,max_length=15)
    telefono_casa = models.CharField(max_length=15)
    telefono_personal = models.CharField(max_length=15)
    dpi = models.CharField(max_length=40)
    seguro = models.CharField(max_length=100)
    descripcion = models.TextField()
    clinica = models.ForeignKey(to='Clinica.Clinica')
    def __str__(self):
        return self.nombres + "," + self.apellidos
    
    @property
    def edad(self):
        return datetime.date.today().year - self.fecha_nacimiento.year 