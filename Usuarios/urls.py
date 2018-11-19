
from django.conf.urls import url,include
from . import views
from django.contrib.auth.decorators import login_required
from .views import CrearUsuario,ListadoUsuario,EditarUsuario,EliminarUsuario,EnvioCorreo
from django.conf.urls import include
""" ejemplo de url: categorias/registrar """

""" los pk en la url de editar y eliminar sirven para saber sobre que dato
se esta trabajando """
urlpatterns = [
    url(r'^crearusuario$', login_required(CrearUsuario.as_view()), name='CrearUsuario'),
    url(r'^listadousuario$', login_required(ListadoUsuario.as_view()), name='ListadoUsuario'),
    url(r'^editarusuario/(?P<pk>\d+)$', login_required(EditarUsuario.as_view()), name='EditarUsuario'),
    url(r'^eliminarusuario/(?P<pk>\d+)$', login_required(EliminarUsuario.as_view()), name='EliminarUsuario'),
]
