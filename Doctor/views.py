from django.shortcuts import render
from django.views.generic.edit import (UpdateView,CreateView,DeleteView)
from django.views.generic import (ListView,DetailView,TemplateView)
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
from .models import Doctor
from .forms import DoctorModelsForms

class CrearDoctor(CreateView):
    model = Doctor
    form_class = DoctorModelsForms
    template_name = 'doctor/CrearDoctor.html'
    success_url = reverse_lazy("doctorUrl:ListadoDoctor")
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.clinica = self.request.user.clinica
        return super(CrearDoctor, self).form_valid(form)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.escritura_doctor():
            messages.success(request, 'No tienes permisos para este apartado!')
            return redirect("inicio")
        return super(CrearDoctor, self).dispatch(request, *args, **kwargs)


class ListadoDoctor(ListView):
    model = Doctor
    template_name = 'doctor/ListadoDoctor.html'
    def get_queryset(self):
        sesion_usuario = self.request.user
        doctors = Doctor.objects.filter(clinica__pk=sesion_usuario.clinica.pk)
        return doctors
    def dispatch(self, request, *args, **kwargs):
        if  not request.user.lectura_doctor():
            messages.success(request, 'No tienes permisos para este apartado!')
            return redirect("inicio")
        return super(ListadoDoctor, self).dispatch(request, *args, **kwargs)

class EditarDoctor(UpdateView):
    model = Doctor
    form_class = DoctorModelsForms
    template_name = 'doctor/EditarDoctor.html'
    success_url = reverse_lazy("doctorUrl:ListadoDoctor")
    def dispatch(self, request, *args, **kwargs):
        if  not request.user.escritura_doctor:
            messages.success(request, 'No tienes permisos para este apartado!')
            return redirect("inicio")
        return super(EditarDoctor, self).dispatch(request, *args, **kwargs)

class EliminarDoctor(DeleteView):
    model = Doctor
    template_name = 'doctor/EliminarDoctor.html'
    success_url = reverse_lazy("doctorUrl:ListadoDoctor")
    def dispatch(self, request, *args, **kwargs):
        if not request.user.eliminacion_doctor:
            messages.success(request, 'No tienes permisos para este apartado!')
            return redirect("inicio")
        return super(EliminarDoctor, self).dispatch(request, *args, **kwargs)
