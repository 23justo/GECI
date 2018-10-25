from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import (ListView,DetailView,TemplateView)
from django.db.models import CharField, Value
import json
from .models import *
from Cita.models import *
# Create your views here.

class BaseContable(TemplateView):
    template_name = 'Contable/BaseContable.html'

def ObtenerMovimientos(request, *args, **kwargs):
    lista_mov_citas = []
    query_movimiento_citas = MovimientoCita.objects.all()
    orden = 0
    for mov_cita in query_movimiento_citas:
        orden+=1
        diccionario = {
            'pk':mov_cita.pk,
            'orden':orden,
            'paciente':mov_cita.cita.paciente.nombres+','+mov_cita.cita.paciente.apellidos,
            'paciente_pk':mov_cita.cita.paciente.pk,
            'monto':mov_cita.monto,
            'fecha':mov_cita.fecha,
            'doctor':mov_cita.cita.doctor.nombres+','+mov_cita.cita.doctor.apellidos,
            'doctor_pk':mov_cita.cita.doctor.pk,
            }
        lista_mov_citas.append(diccionario)
    return JsonResponse(json.dumps(lista_mov_citas),safe=False)

def ObtenerMovimientoEspecifico(request, *args, **kwargs):
    lista_mov_citas = []
    mov_cita = MovimientoCita.objects.get(pk=kwargs['pk'])
    diccionario = {
        
        'fecha':mov_cita.fecha,
        #informacion doctor
        'doctor_nombres':mov_cita.cita.doctor.nombres,
        'doctor_apellidos':mov_cita.cita.doctor.apellidos,
        'telefono':mov_cita.cita.doctor.telefono,
        'especialidad':mov_cita.cita.doctor.especialidad,
        'direccion_clinica':mov_cita.cita.doctor.direccion_clinica,
        'dpi':mov_cita.cita.doctor.dpi,
        #informacion paciente
        'paciente_nombres':mov_cita.cita.paciente.nombres,
        'paciente_apellidos':mov_cita.cita.paciente.apellidos,
        'sexo ':mov_cita.cita.paciente.sexo,
        'edad':mov_cita.cita.paciente.edad,
        'tipo_sangre':mov_cita.cita.paciente.tipo_sangre,
        'telefono_casa':mov_cita.cita.paciente.telefono_casa,
        'telefono_personal':mov_cita.cita.paciente.telefono_personal,
        'dpi':mov_cita.cita.paciente.dpi,
        'seguro':mov_cita.cita.paciente.seguro,
        'descripcion':mov_cita.cita.paciente.descripcion,
        #informacion cita
        'cita_descripcion':mov_cita.cita.descripcion,
        'cita_fecha_inicio':mov_cita.cita.fecha_inicio_formato,
        'cita_fecha_fin':mov_cita.cita.fecha_fin_formato,
        'cita_monto':mov_cita.monto,
    }
    lista_mov_citas.append(diccionario)
    return JsonResponse(json.dumps(lista_mov_citas),safe=False)