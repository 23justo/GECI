from django.contrib import admin

from .models import Cita
from .forms import CitaModelsForms
# Register your models here.

class CitaAdmin(admin.ModelAdmin):
    list_display = [
    'id'   ,
    'fecha_inicio',
    'fecha_fin',
    'doctor',
    'paciente',
    'descripcion',
    ]
    form = CitaModelsForms

admin.site.register(Cita,CitaAdmin)
