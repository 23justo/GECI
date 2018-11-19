from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.edit import (UpdateView,CreateView,DeleteView)
from django.views.generic import (ListView,DetailView,TemplateView)
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from .models import Paciente
from .forms import PacienteModelsForms

class CrearPaciente(CreateView):
    model = Paciente
    form_class = PacienteModelsForms
    template_name = 'paciente/CrearPaciente.html'
    success_url = reverse_lazy("pacienteUrl:ListadoPaciente")
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.clinica = self.request.user.clinica
        return super(CrearPaciente, self).form_valid(form)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.escritura_paciente():
            messages.success(request, 'No tienes permisos para este apartado!')
            return redirect("inicio")
        return super(CrearPaciente, self).dispatch(request, *args, **kwargs)


class ListadoPaciente(ListView):
    model = Paciente
    template_name = 'paciente/ListadoPaciente.html'
    def get_queryset(self):
        sesion_usuario = self.request.user
        pacientes = Paciente.objects.filter(clinica__pk=sesion_usuario.clinica.pk)
        return pacientes
    def dispatch(self, request, *args, **kwargs):
        if not request.user.lectura_paciente():
            messages.success(request, 'No tienes permisos para este apartado!')
            return redirect("inicio")
        return super(ListadoPaciente, self).dispatch(request, *args, **kwargs)

class EditarPaciente(UpdateView):
    model = Paciente
    form_class = PacienteModelsForms
    template_name = 'paciente/EditarPaciente.html'
    success_url = reverse_lazy("pacienteUrl:ListadoPaciente")
    def dispatch(self, request, *args, **kwargs):
        if not request.user.escritura_paciente():
            messages.success(request, 'No tienes permisos para este apartado!')
            return redirect("inicio")
        return super(EditarPaciente, self).dispatch(request, *args, **kwargs)

class EliminarPaciente(DeleteView):
    model = Paciente
    template_name = 'paciente/EliminarPaciente.html'
    success_url = reverse_lazy("pacienteUrl:ListadoPaciente")
    def dispatch(self, request, *args, **kwargs):
        if not request.user.eliminacion_paciente():
            messages.success(request, 'No tienes permisos para este apartado!')
            return redirect("inicio")
        return super(EliminarPaciente, self).dispatch(request, *args, **kwargs)
