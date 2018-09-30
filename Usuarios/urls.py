
from django.conf.urls import url,include
from . import views
from django.contrib.auth.decorators import login_required
from .views import CrearUsuario,ListadoUsuario

""" ejemplo de url: categorias/registrar """

""" los pk en la url de editar y eliminar sirven para saber sobre que dato
se esta trabajando """
urlpatterns = [
    url(r'^crearusuario$', login_required(CrearUsuario.as_view()), name='CrearUsuario'),
    url(r'^listadousuario$', login_required(ListadoUsuario.as_view()), name='ListadoUsuario'),

]
