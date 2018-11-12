from django.shortcuts import render
from django.views.generic.edit import (UpdateView,CreateView,DeleteView)
from django.views.generic import (ListView,DetailView,TemplateView)
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from .models import Cita
from .forms import CitaModelsForms

class CrearCita(CreateView):
    model = Cita
    form_class = CitaModelsForms
    template_name = 'cita/CrearCita.html'
    success_url = reverse_lazy("citaUrl:ListadoCita")
    # El formulario se crea utilizando filtros aplicados a los querys de pacientes y doctores
    def get_form_kwargs(self):
        kwargs = super(CrearCita, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ListadoCita(ListView):
    model = Cita
    template_name = 'cita/ListadoCita.html'

class EditarCita(UpdateView):
    model = Cita
    form_class = CitaModelsForms
    template_name = 'cita/EditarCita.html'
    success_url = reverse_lazy("citaUrl:ListadoCita")
    # El formulario se crea utilizando filtros aplicados a los querys de pacientes y doctores
    def get_form_kwargs(self):
        kwargs = super(EditarCita, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class EliminarCita(DeleteView):
    model = Cita
    template_name = 'cita/EliminarCita.html'
    success_url = reverse_lazy("citaUrl:ListadoCita")

class VerCita(DetailView):
    model = Cita
    template_name = 'cita/VerCita.html'
    



