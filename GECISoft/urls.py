"""GECISoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Usuarios.views import InicioView
from django.contrib.auth.views import login,logout_then_login,logout
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login',login,{'template_name':'templates/login.html'},name='login'),
    url(r'^logout',logout,{'next_page':'login'},name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
]

urlpatterns += i18n_patterns(
    url(r'^$', login_required(InicioView.as_view()),name='inicio'),
    url(r'^administrador/',include('Usuarios.urls', namespace='adminUrl') ),
    url(r'^clinica/',include('Clinica.urls', namespace='clinicaUrl') ),
    url(r'^paciente/',include('Paciente.urls', namespace='pacienteUrl') ),
    url(r'^cita/',include('Cita.urls', namespace='citaUrl') ),
    url(r'^doctor/',include('Doctor.urls', namespace='doctorUrl') ),
    url(r'^movimientocita/',include('Contable.urls', namespace='movimientocitaUrl') ),
)
