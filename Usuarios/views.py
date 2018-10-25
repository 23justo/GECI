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

##### Importaciones Propias
from .models import Usuario
from .forms import UserCreationForm,UserChangeForm
# Create your views here.

class InicioView(TemplateView):
    template_name = "templates/index.html"

class CrearUsuario(CreateView):
    model = Usuario
    form_class = UserCreationForm
    template_name = 'administrador/CrearUsuario.html'
    success_url = reverse_lazy("adminUrl:ListadoUsuario")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin():
            messages.success(request, 'No tienes permisos para este apartado!')
            return redirect("inicio")
        return super(CrearUsuario, self).dispatch(request, *args, **kwargs)

class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuarios/ListadoUsuario.html'

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
    















def hola():
    return 1
