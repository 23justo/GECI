from django.shortcuts import render
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


class ListadoPaciente(ListView):
    model = Paciente
    template_name = 'paciente/ListadoPaciente.html'
    def get_queryset(self):
        sesion_usuario = self.request.user
        pacientes = Paciente.objects.filter(clinica__pk=sesion_usuario.clinica.pk)
        print(pacientes)
        return pacientes

class EditarPaciente(UpdateView):
    model = Paciente
    form_class = PacienteModelsForms
    template_name = 'paciente/EditarPaciente.html'
    success_url = reverse_lazy("pacienteUrl:ListadoPaciente")

class EliminarPaciente(DeleteView):
    model = Paciente
    template_name = 'paciente/EliminarPaciente.html'
    success_url = reverse_lazy("pacienteUrl:ListadoPaciente")
