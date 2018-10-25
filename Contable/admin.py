from django.contrib import admin
from .models import MovimientoCita
from .forms import MovimientoCitaModelsForms
# Register your models here.

class MovimientoCitaAdmin(admin.ModelAdmin):
    list_display = [
    'id',
    'cita',
    'monto',
    'pagado',
    'creado',
    'modificado',
    ]
    form = MovimientoCitaModelsForms

admin.site.register(MovimientoCita,MovimientoCitaAdmin)
