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
from .models import Estado, Seguimiento

class EstadoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

class SeguimientoAdmin(admin.ModelAdmin):
	list_display  = ('pregunta', 'estado', 'fecha')
	list_filter   = ('estado', 'pregunta')
	search_fields = ('estado', 'pregunta')

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Seguimiento, SeguimientoAdmin)