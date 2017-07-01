# -*- coding: utf-8 -*-
##########################################################################
####     Copyright 2013 SASIF NC -  Todos los Derechos reservados     ####
####                       www.sasifnc.com                            ####
#### Se prohibe la divulgación, utilización, transmisión,             ####
#### distribución, reproducción y transformación, total o parcial,    ####
#### en cualquier soporte o medio, de los contenidos de este software ####
#### sin previa autorización de SASIF NC.                             #### 
##########################################################################
from django.contrib import admin

#MODELOS
from .models import preguntaTemporal, Solicitud, Categoria

class SolicitudAdmin(admin.ModelAdmin):
	list_display  = ('fecha', 'pregunta', 'institucion', 'categoria', 'publicado')
	list_filter   = ('publicado', 'institucion', 'categoria')
	search_fields = ('publicado', 'institucion', 'categoria')

admin.site.register(Solicitud, SolicitudAdmin)

admin.site.register(preguntaTemporal)
admin.site.register(Categoria)

