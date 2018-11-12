from django.conf.urls import url,include
from . import views
from django.contrib.auth.decorators import login_required
from .views import CrearCita,ListadoCita,EditarCita,EliminarCita,VerCita

""" ejemplo de url: categorias/registrar """

""" los pk en la url de editar y eliminar sirven para saber sobre que dato
se esta trabajando """
urlpatterns = [
    url(r'^crearcita$', login_required(CrearCita.as_view()), name='CrearCita'),
    url(r'^listadocita$', login_required(ListadoCita.as_view()), name='ListadoCita'),
    url(r'^editarcita/(?P<pk>\d+)$', login_required(EditarCita.as_view()), name='EditarCita'),
    url(r'^eliminarcita/(?P<pk>\d+)$', login_required(EliminarCita.as_view()), name='EliminarCita'),
    url(r'^vercita/(?P<pk>\d+)$', login_required(VerCita.as_view()), name='VerCita'),
]
