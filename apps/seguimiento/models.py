# -*- coding: utf-8 -*-
##########################################################################
####     Copyright 2014 CMAGINET -  Todos los Derechos reservados     ####
####                       www.cmaginet.com                           ####
#### Se prohibe la divulgación, utilización, transmisión,             ####
#### distribución, reproducción y transformación, total o parcial,    ####
#### en cualquier soporte o medio, de los contenidos de este software ####
#### sin previa autorización de CMAGINET.                             ####
##########################################################################
from django.db import models

from autoslug import AutoSlugField
from colorfield.fields import ColorField

#MODELOS
from apps.solicitudes.models import Solicitud

class Estado(models.Model):
	nombre = models.CharField(max_length=300)
	color  = ColorField()
	slug   = AutoSlugField(populate_from='nombre', always_update=True, unique=True)

	class Meta:
		verbose_name = "Estado de Seguimiento"
		verbose_name_plural = "Estados de Seguimientos"

	def __unicode__(self):
		return u'%s' % (self.nombre)

class Seguimiento(models.Model):
	pregunta   = models.ForeignKey(Solicitud)
	estado     = models.ForeignKey(Estado)
	fecha      = models.DateField()
	comentario = models.TextField()
	documento  = models.FileField(upload_to='seguimiento', blank=True, null=True)

	class Meta:
		verbose_name = "Seguimiento a solicitud de información"
		verbose_name_plural = "Seguimiento a solicitudes de información"

	def __unicode__(self):
		return u'%s' % (self.pregunta)
