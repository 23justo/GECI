from django.conf.urls import url,include
from . import views
from django.contrib.auth.decorators import login_required
from .views import CrearDoctor,ListadoDoctor,EditarDoctor,EliminarDoctor

""" ejemplo de url: categorias/registrar """

""" los pk en la url de editar y eliminar sirven para saber sobre que dato
se esta trabajando """
urlpatterns = [
    url(r'^creardoctor$', login_required(CrearDoctor.as_view()), name='CrearDoctor'),
    url(r'^listadodoctor$', login_required(ListadoDoctor.as_view()), name='ListadoDoctor'),
    url(r'^editardoctor/(?P<pk>\d+)$', login_required(EditarDoctor.as_view()), name='EditarDoctor'),
    url(r'^eliminardoctor/(?P<pk>\d+)$', login_required(EliminarDoctor.as_view()), name='EliminarDoctor'),
]
