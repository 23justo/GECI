from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (Usuario,)
# Register your models here.

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', '__unicode__', 'username','nombres','apellidos', 'email','telefono', 'ultima_conexion','visible',]

admin.site.register(Usuario,UsuarioAdmin)
