from django.shortcuts import render
from django.views.generic.edit import (UpdateView,CreateView,DeleteView)
from django.views.generic import (ListView,DetailView,TemplateView)
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from .models import Clinica
from .forms import ClinicaModelsForms
from Contable.models import *
from django.utils.http import *
import json
import urllib.request

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
    fields = [
        "nombre","direccion","telefono",
        'moneda','color_menu','color_footer',
        'color_texto_menu',
    ]
    template_name = 'clinica/EditarClinica.html'
    success_url = reverse_lazy("clinicaUrl:ListadoClinica")
    def form_valid(self,form):
        clinica_info_anterior = Clinica.objects.get(pk = self.object.pk)
        if not self.object.moneda == clinica_info_anterior.moneda:
            conversion_moneda(clinica_info_anterior.pk,clinica_info_anterior.moneda,self.object.moneda)
        return super(EditarClinica, self).form_valid(form)

def conversion_moneda(clinica_pk,moneda_anterior,moneda_nueva):
    url = "http://data.fixer.io/api/latest?access_key=4a593cbbc348f0d8ac75a14a149094b7"
    req = urllib.request.Request(url,headers={'User-Agent': 'howCode Currency Bot'})
    data = urllib.request.urlopen(req).read()
    data = json.loads(data.decode('utf-8'))
    print(data)
    rates = data["rates"]

    movimientos = MovimientoCita.objects.filter(cita__doctor__clinica__pk = clinica_pk)
    for movimiento in movimientos:
        print("1")
        print(movimiento.monto)
        movimiento.monto = movimiento.monto * rates[moneda_nueva]
        movimiento.save(update_fields=["monto"]) 
        print("2")
        print(movimiento.monto)
        
        
    

class EliminarClinica(DeleteView):
    model = Clinica
    template_name = 'clinica/EliminarClinica.html'
    success_url = reverse_lazy("clinicaUrl:ListadoClinica")
