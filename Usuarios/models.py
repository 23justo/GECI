from django.db import models
from django.conf import settings
from django.contrib import auth
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin,BaseUserManager
# Create your models here

class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None,email=None):
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
        ('Prueba','Prueba'),
    )
    tipos_permisos = (
        (1,'Lectura'),
        (2,'Escritura'),
        (3,'Eliminacion'),
        (4,'Todos'),
    )
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 45,unique = True)
    nombres = models.CharField(max_length = 150)
    apellidos = models.CharField(max_length = 150)
    especialidad = models.CharField(max_length = 150)
    email = models.EmailField(null=True)
    telefono = models.CharField(max_length = 12)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    ultima_conexion = models.DateTimeField(auto_now_add=True, auto_now=False)
    user_type = models.CharField(max_length=45,choices=user_types,default="Prueba")
    visible = models.BooleanField(default=True)
    # la clinica con id 1 solo sirve para poder asignar a los admin 
    clinica = models.ForeignKey(to='Clinica.Clinica',default=1)
    modulo_doctor = models.IntegerField(choices=tipos_permisos,null=True)
    modulo_citas = models.IntegerField(choices=tipos_permisos,null=True)
    modulo_paciente = models.IntegerField(choices=tipos_permisos,null=True)
    modulo_contable = models.IntegerField(choices=tipos_permisos,null=True)
    modulo_secretaria = models.IntegerField(choices=tipos_permisos,null=True)
    modulo_usuario = models.IntegerField(choices=tipos_permisos,null=True)
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
    def is_prueba(self):
        if self.user_type=="Prueba":
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
    #permisos doctor
    def lectura_doctor(self):
        if self.modulo_doctor == 4 or self.modulo_doctor == 1:
            return True
        else:
            return False
    
    def escritura_doctor(self):
        if self.modulo_doctor == 4 or self.modulo_doctor == 2:
            return True
        else:
            return False
    def eliminacion_doctor(self):
        if self.modulo_doctor == 4 or self.modulo_doctor == 3:
            return True
        else:
            return False
    #fin permisos doctor
    #permisos citas
    def lectura_citas(self):
        if self.modulo_citas == 4 or self.modulo_citas == 1:
            return True
        else:
            return False
    
    def escritura_citas(self):
        if self.modulo_citas == 4 or self.modulo_citas == 2:
            return True
        else:
            return False
    def eliminacion_citas(self):
        if self.modulo_citas == 4 or self.modulo_citas == 3:
            return True
        else:
            return False
    #fin permisos citas
    #permisos paciente
    def lectura_paciente(self):
        if self.modulo_paciente == 4 or self.modulo_paciente == 1:
            return True
        else:
            return False
    
    def escritura_paciente(self):
        if self.modulo_paciente == 4 or self.modulo_paciente == 2:
            return True
        else:
            return False
    def eliminacion_paciente(self):
        if self.modulo_paciente == 4 or self.modulo_paciente == 3:
            return True
        else:
            return False
    #fin permisos paciente
    #permisos contable
    def lectura_contable(self):
        if self.modulo_contable == 4 or self.modulo_contable == 1:
            return True
        else:
            return False
    
    def escritura_contable(self):
        if self.modulo_contable == 4 or self.modulo_contable == 2:
            return True
        else:
            return False
    def eliminacion_contable(self):
        if self.modulo_contable == 4 or self.modulo_contable == 3:
            return True
        else:
            return False
    #fin permisos contable

    
    


    def has_module_perms(self,perm_list):
        return self.is_staff
    def has_perm(self,perm):
    	return True
