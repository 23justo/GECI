from django import forms
from .models import Clinica
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ClinicaModelsForms(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = [
        'nombre',
        'direccion',
        'telefono'
        ]
