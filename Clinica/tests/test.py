from mixer.backend.django import mixer
import pytest

class TestModels:
    def default_return_value(self):
        clinica = mixer.blend('Clinica.Clinica',nombre='clinica_test')
        assert len(product.str ) < 0