from django import forms
from .models import Solicitudes
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class SolicitudesModelsForms(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = [
        'correo',
        'nombre_completo',
        'tema',
        'mensaje',
        ]
