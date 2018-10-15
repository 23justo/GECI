from django.db import models

# Create your models here.
class Cita(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    doctor = models.ForeignKey(to='Doctor.Doctor')
    paciente = models.ForeignKey(to='Paciente.Paciente')
    descripcion = models.TextField()
    def __str__(self):
        return self.fecha_inicio + self.fecha_fin + self.doctor