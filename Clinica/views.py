from django.shortcuts import render
from django.views.generic.edit import (UpdateView,CreateView,DeleteView)
from django.views.generic import (ListView,DetailView,TemplateView)
# Create your views here.
from .models import Clinica
from .forms import ClinicaModelsForms

class CrearClinica(CreateView):
    model = Clinica
    form_class = ClinicaModelsForms
    template_name = 'clinica/CrearClinica.html'
    success_url = "/"

class ListadoClinica(ListView):
    model = Clinica
    template_name = 'clinica/ListadoClinica.html'
