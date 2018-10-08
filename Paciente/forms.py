from django import forms
from .models import Paciente

class PacienteModelsForms(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
        'nombres', 'apellidos',
        'sexo','fecha_nacimiento','tipo_sangre',
        'telefono_casa','telefono_personal','dpi',
        'seguro','descripcion',
        ]
