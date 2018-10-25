from django.conf.urls import url,include
from . import views
from django.contrib.auth.decorators import login_required
from .views import CrearPaciente,ListadoPaciente,EditarPaciente,EliminarPaciente

""" ejemplo de url: categorias/registrar """

""" los pk en la url de editar y eliminar sirven para saber sobre que dato
se esta trabajando """
urlpatterns = [
    url(r'^crearpaciente$', login_required(CrearPaciente.as_view()), name='CrearPaciente'),
    url(r'^listadopaciente$', login_required(ListadoPaciente.as_view()), name='ListadoPaciente'),
    url(r'^editarpaciente/(?P<pk>\d+)$', login_required(EditarPaciente.as_view()), name='EditarPaciente'),
    url(r'^eliminarpaciente/(?P<pk>\d+)$', login_required(EliminarPaciente.as_view()), name='EliminarPaciente'),
]
