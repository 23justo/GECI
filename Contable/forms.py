from django import forms
from .models import MovimientoCita

class MovimientoCitaModelsForms(forms.ModelForm):
    class Meta:
        model = MovimientoCita
        fields = [
        'cita',
        'monto',
        'pagado',
        ]
