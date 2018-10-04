from django.conf.urls import url,include
from . import views
from django.contrib.auth.decorators import login_required
from .views import CrearClinica,ListadoClinica

""" ejemplo de url: categorias/registrar """

""" los pk en la url de editar y eliminar sirven para saber sobre que dato
se esta trabajando """
urlpatterns = [
    url(r'^crearclinica$', login_required(CrearClinica.as_view()), name='CrearClinica'),
    url(r'^listadoclinica$', login_required(ListadoClinica.as_view()), name='ListadoClinica'),


]
