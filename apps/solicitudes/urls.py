# -*- coding: utf-8 -*-
##########################################################################
####     Copyright 2014 CMAGINET -  Todos los Derechos reservados     ####
####                       www.cmaginet.com                           ####
#### Se prohibe la divulgación, utilización, transmisión,             ####
#### distribución, reproducción y transformación, total o parcial,    ####
#### en cualquier soporte o medio, de los contenidos de este software ####
#### sin previa autorización de CMAGINET.                             ####
##########################################################################

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from .views import preguntaTemporalProcesarView, solicitudesListView, solicitudesDetailView, loguearUsuarioEmail

# VISTAS AJAX
from .views import preguntaTemporalGuardarView

urlpatterns = patterns('',
	url(r'^archivo/$',solicitudesListView.as_view(), name='solicitudes-listado'),
	url(r'^archivo/(?P<categoria>[-\w]+)/$', solicitudesListView.as_view(), name='solicitudes-listado-categoria'),
	url(r'^archivo/buscar/(?P<buscar>[-\w\s]+)/$', solicitudesListView.as_view(), name='solicitudes-listado-buscar'),
	url(r'^archivo/solicitud/(?P<slug>[-\w]+)/$', solicitudesDetailView.as_view(), name='solicitudes-detalle'),
	url(r'^archivo/solicitud/(?P<slug>[-\w]+)/(?P<token>\w+)/$', solicitudesDetailView.as_view(), name='solicitudes-detalle-token'),

	url(r'^archivo/loguear/(?P<slug>[-\w]+)/$', loguearUsuarioEmail, name='solicitudes-loguear-email'),

	url(r'^pregunta/temporal/procesar/(?P<token>\w+)/$', login_required(preguntaTemporalProcesarView.as_view()), name='solicitudes-pregunta-temporal-procesar'),
	

	#AJAX
	url(r'^pregunta/temporal/guardar/$', preguntaTemporalGuardarView, name='solicitudes-pregunta-temporal-nuevo'),
)