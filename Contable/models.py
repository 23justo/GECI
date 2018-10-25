from django.db import models

# Create your models here.
class MovimientoCita(models.Model):
    cita = models.ForeignKey(to='Cita.Cita')
    monto = models.FloatField()
    pagado = models.BooleanField()
    creado = models.DateTimeField(auto_now=True)
    modificado = models.DateTimeField(auto_now=True)
    
    @property
    def fecha(self):
        return self.cita.fecha_inicio.strftime("%d %m %Y")

    