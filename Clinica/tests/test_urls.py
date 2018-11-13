from django.urls import reverse, resolve
from mixer.backend.django import mixer
import pytest

class TestUrls:
    def test_detail_url(self):
        path = reverse('clinicaUrl:CrearClinica')
        print(path)
        assert resolve(path).view_name == 'clinicaUrl:CrearClinica'

    def default_return_value(self):
        clinica = mixer.blend('Clinica.Clinica',nombre='clinica_test')
        assert len(product.str ) < 0