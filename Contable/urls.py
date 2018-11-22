from django.conf.urls import url,include
from . import views
from django.contrib.auth.decorators import login_required
# from .views import CrearMovimientoCita,ListadoMovimientoCita,EditarMovimientoCita,EliminarMovimientoCita
from .views import BaseContable,ObtenerMovimientos,ObtenerMovimientoEspecifico,CrearMovimientoCita,ObtenerMoneda


""" ejemplo de url: categorias/registrar """

""" los pk en la url de editar y eliminar sirven para saber sobre que dato
se esta trabajando """
urlpatterns = [
url(r'^basecontable$', login_required(BaseContable.as_view()), name='BaseContable'),
# retorna un json con los movimientos solicitados
url(r'^api-ObtenerMovimientos$', ObtenerMovimientos, name='api-ObtenerMovimientos'),
url(r'^api-ObtenerMovimientoEspecifico/(?P<pk>\d+)$', ObtenerMovimientoEspecifico, name='api-ObtenerMovimientoEspecifico'),
url(r'^api-ObtenerMoneda$', ObtenerMoneda, name='api-ObtenerMoneda'),


url(r'^crearmovimientocita/(?P<pk>\d+)$', login_required(CrearMovimientoCita.as_view()), name='CrearMovimientoCita'),
# url(r'^listadomovimientocita$', login_required(ListadoMovimientoCita.as_view()), name='ListadoMovimientoCita'),
# url(r'^editarmovimientocita/(?P<pk>\d+)$', login_required(EditarMovimientoCita.as_view()), name='EditarMovimientoCita'),
# url(r'^eliminarmovimientocita/(?P<pk>\d+)$', login_required(EliminarMovimientoCita.as_view()), name='EliminarMovimientoCita'),
]
