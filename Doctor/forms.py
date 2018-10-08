from django import forms
from .models import Doctor
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class DoctorModelsForms(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
        'id',
        'nombres',
        'apellidos',
        'telefono',
        'fecha_nacimiento',
        'sexo',
        'especialidad',
        'direccion_clinica',
        'dpi',
        ]
