from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import (UpdateView,CreateView,DeleteView)
from django.views.generic import (ListView,DetailView,TemplateView)
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from .models import Solicitudes
from .forms import SolicitudesModelsForms
from django.contrib import messages
# Create your views here.

class ListadoSolicitudes(ListView):
    model = Solicitudes
    template_name = 'solicitudes/ListadoSolicitudes.html'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin():
            messages.success(request, 'No tienes permisos para este apartado!')
            return redirect("inicio")
        return super(ListadoSolicitudes, self).dispatch(request, *args, **kwargs)