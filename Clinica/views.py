from django.shortcuts import render
from django.views.generic.edit import (UpdateView,CreateView,DeleteView)
from django.views.generic import (ListView,DetailView,TemplateView)
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from .models import Clinica
from .forms import ClinicaModelsForms

class CrearClinica(CreateView):
    model = Clinica
    form_class = ClinicaModelsForms
    template_name = 'clinica/CrearClinica.html'
    success_url = reverse_lazy("clinicaUrl:ListadoClinica")

class ListadoClinica(ListView):
    model = Clinica
    template_name = 'clinica/ListadoClinica.html'

class EditarClinica(UpdateView):
    model = Clinica
    fields = ["nombre","direccion","telefono"]
    template_name = 'clinica/EditarClinica.html'
    success_url = reverse_lazy("clinicaUrl:ListadoClinica")

class EliminarClinica(DeleteView):
    model = Clinica
    template_name = 'clinica/EliminarClinica.html'
    success_url = reverse_lazy("clinicaUrl:ListadoClinica")
