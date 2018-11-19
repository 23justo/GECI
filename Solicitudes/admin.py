from django.contrib import admin
from .models import Solicitudes
from .forms import SolicitudesModelsForms
# Register your models here.

class SolicitudesAdmin(admin.ModelAdmin):
    list_display = [
    'id',
    'correo',
    'nombre_completo',
    'tema',
    'mensaje',
    ]
    

admin.site.register(Solicitudes,SolicitudesAdmin)
