from django.db import models
from django.conf import settings
from django.contrib import auth
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin,BaseUserManager
# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Ingrese un nombre de usuario valido.')
        usuario = self.model(
            username = username,
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self, username, password=None):
        usuario = self.create_user(username, password)
        usuario.is_staff = True
        usuario.set_password(password)
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    user_types = (
        ('Admin','Admin'),
        ('Doctor','Doctor'),
        ('Secretaria','Secretaria'),
    )
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 45,unique = True)
    nombres = models.CharField(max_length = 150)
    apellidos = models.CharField(max_length = 150)
    especialidad = models.CharField(max_length = 150)
    email = models.EmailField()
    telefono = models.CharField(max_length = 12)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    ultima_conexion = models.DateTimeField(auto_now_add=True, auto_now=False)
    user_type = models.CharField(max_length=45,choices=user_types,default="Admin")
    visible = models.BooleanField(default=True)
    clinica = models.ForeignKey(to='Clinica.Clinica')
    objects = UsuarioManager()
    USERNAME_FIELD = 'username'
    def get_short_name(self):
        return self.nombres + self.apellidos
    def get_type(self):
        return self.user_type
    def is_admin(self):
        if self.user_type=="Admin":
            return True
        else:
            return False
    def is_doctor(self):
        if self.user_type=="Doctor":
            return True
        else:
            return False

    def is_contador(self):
        if self.user_type=="Secretaria":
            return True
        else:
            return False

    def __unicode__(self):
    	return self.nombres
    def __str__(self):
    	return self.nombres


    def has_module_perms(self,perm_list):
        return self.is_staff
    def has_perm(self,perm):
    	return True
