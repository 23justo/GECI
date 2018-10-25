from django import forms
from .models import Cita
from Doctor.models import Doctor
from Paciente.models import Paciente
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class CitaModelsForms(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
        'fecha_inicio','fecha_fin','doctor',
        'descripcion','paciente'
        ]
    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(CitaModelsForms, self).__init__(*args, **kwargs)
       self.fields['doctor'].queryset = Doctor.objects.filter(clinica=user.clinica)
       self.fields['paciente'].queryset = Paciente.objects.filter(clinica=user.clinica)

