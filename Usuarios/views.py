from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic import ListView, TemplateView,View,DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.dispatch import receiver
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import View
from django.core.validators import validate_email
from django.http import JsonResponse
from django.contrib import messages
from .models import Usuario

from Doctor.models import Doctor
from Paciente.models import Paciente
from Usuarios.models import Usuario
from Contable.models import MovimientoCita
from Cita.models import Cita


##### Importaciones Propias
from .models import Usuario
from .forms import UserCreationForm,UserChangeForm
# Create your views here.
class ActivityMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ActivityMixin, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['doctor'] = Doctor.objects.filter(clinica = self.request.user.clinica)
        context['pacientes'] = Paciente.objects.filter(clinica = self.request.user.clinica)
        context['usuarios'] = Usuario.objects.filter(clinica = self.request.user.clinica)
        context['secretaria'] = Usuario.objects.filter(clinica = self.request.user.clinica).filter(user_type='Secretaria')
        
        
        return context

class InicioView(ActivityMixin,TemplateView):
    template_name = "templates/inicio.html"
    def dispatch(self, request, *args, **kwargs):
        if  request.user.is_prueba():
            messages.success(request, 'No tienes permisos para este apartado!')
            print(messages)
            return redirect("logout")
        return super(InicioView, self).dispatch(request, *args, **kwargs)

        
class CrearUsuario(CreateView):
    model = Usuario
    form_class = UserCreationForm
    template_name = 'administrador/CrearUsuario.html'
    success_url = reverse_lazy("adminUrl:ListadoUsuario")
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin():
            messages.success(request, 'No tienes permisos para este apartado!')
            return redirect("inicio")
        elif request.user.modulo_usuario < 1:
            messages.success(request, 'No tienes permisos para este apartado!')
            return redirect("inicio")
        return super(CrearUsuario, self).dispatch(request, *args, **kwargs)

class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuarios/ListadoUsuario.html'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff == True:
            messages.warning(request, "No tienes permisos para acceder a este apartado")
            return redirect('inicio')
        return super(ListadoUsuario, self).dispatch(request, *args, **kwargs)

class EditarUsuario(UpdateView):
    model = Usuario
    fields = ["nombres","apellidos","username","user_type",
              "email","telefono","clinica","is_staff"
    ]
    template_name = 'usuarios/EditarUsuario.html'
    success_url = reverse_lazy("adminUrl:ListadoUsuario")

class EliminarUsuario(DeleteView):
    model = Usuario
    template_name = 'usuarios/EliminarUsuario.html'
    success_url = reverse_lazy("adminUrl:ListadoUsuario")



