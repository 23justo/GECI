from django.contrib import admin

from .models import Doctor
from .forms import DoctorModelsForms
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = [
    'id',
    'nombres',
    'apellidos',
    'telefono',
    'fecha_nacimiento',
    'clinica',
    ]
    

admin.site.register(Doctor,DoctorAdmin)
