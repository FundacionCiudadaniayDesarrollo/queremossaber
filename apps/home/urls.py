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

#VISTAS
from .views import portalHome, portalIniciativa, portaltuDerecho, portalLotaip, portalContact, portalContactResponse, logout_view

urlpatterns = patterns('',
	url(r'^$', portalHome.as_view(), name='home-portal-home'),

	#blog
	url(r'^sobre-la-iniciativa/$', portalIniciativa.as_view(), name='home-portal-iniciativa'),
	url(r'^tu-derecho-a-saber/$', portaltuDerecho.as_view(), name='home-portal-derecho'),
	url(r'^lotaip/$', portalLotaip.as_view(), name='home-portal-lotaip'),
	url(r'^contactenos/$', portalContact.as_view(), name='portal-home-contact'),
	url(r'^contactenos/success/$', portalContactResponse.as_view(), name='portal-home-contact-response'),

	url(r'^salir/$', logout_view, name='portal-home-salir'),
)