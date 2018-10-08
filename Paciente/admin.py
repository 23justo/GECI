from django.contrib import admin
from .models import (Paciente,)

# Register your models here.
class PacienteAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'nombres', 'apellidos',
        'sexo','fecha_nacimiento','tipo_sangre',
        'telefono_casa','telefono_personal','dpi',
        'seguro','descripcion',
    ]



admin.site.register(Paciente,PacienteAdmin)
