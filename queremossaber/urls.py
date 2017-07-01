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
from django.conf.urls.static import static
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from vanilla import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(url=reverse_lazy('home-portal-home'))),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^portal/', include('apps.home.urls')),
	url(r'^portal/accounts/', include('allauth.urls')),
	url(r'^portal/solicitudes/', include('apps.solicitudes.urls')),
	#Social Auth
	url('', include('social.apps.django_app.urls', namespace='social')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)