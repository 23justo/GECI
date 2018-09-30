from django.contrib import admin

from .models import Clinica
from .forms import ClinicaModelsForms
# Register your models here.

class ClinicaAdmin(admin.ModelAdmin):
    list_display = [
    'id',
    'nombre',
    'direccion',
    'telefono'
    ]
    form = ClinicaModelsForms

admin.site.register(Clinica,ClinicaAdmin)
