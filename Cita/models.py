from django.db import models

# Create your models here.
class Cita(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    doctor = models.ForeignKey(to='Doctor.Doctor')
    paciente = models.ForeignKey(to='Paciente.Paciente')
    descripcion = models.TextField()
    @property
    def fecha_inicio_formato(self):
        return self.fecha_inicio.strftime("%d %m %Y")
    
    @property
    def fecha_fin_formato(self):
        return self.fecha_fin.strftime("%d %m %Y")
    