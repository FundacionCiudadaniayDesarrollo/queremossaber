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

from uuidfield import UUIDField
from autoslug import AutoSlugField
from colorfield.fields import ColorField

#MODELOS
from django.contrib.auth.models import User

class preguntaTemporal(models.Model):
	pregunta    = models.TextField()
	institucion = models.CharField(max_length=300)
	token       = UUIDField(auto=True)
	
	class Meta:
		verbose_name = "Pregunta Temporal"
		verbose_name_plural = "Preguntas Temporales"

	def __unicode__(self):
		return u'%s' % (self.token)	

class Categoria(models.Model):
	nombre = models.CharField(max_length=300)
	color  = ColorField()
	slug   = AutoSlugField(populate_from='nombre', always_update=True, unique=True)

	class Meta:
		verbose_name = "Categoría"
		verbose_name_plural = "Categorías"

	def __unicode__(self):
		return u'%s' % (self.nombre)

class Solicitud(models.Model):
	fecha       = models.DateTimeField(auto_now_add=True)
	pregunta    = models.TextField()
	institucion = models.CharField(max_length=300, blank=True, null=True)
	categoria   = models.ForeignKey(Categoria, blank=True, null=True)
	usuario     = models.ForeignKey(User)
	seguidores  = models.ManyToManyField(User, related_name='usuarios_seguidores', blank=True, null=True)
	token       = models.CharField(max_length=400)
	publicado   = models.BooleanField(default=False)
	slug        = AutoSlugField(max_length=100, populate_from='pregunta', always_update=True, unique=True)

	@property
	def estado(self):
		seguimiento = self.seguimiento_set.filter(pregunta=self).latest('fecha')
		return seguimiento.estado

	@property
	def number_seguidores(self):
		seguidores = self.seguidores.all().count()
		return seguidores

	class Meta:
		verbose_name = "Solicitud de información"
		verbose_name_plural = "Solicitudes de información"

	def __unicode__(self):
		return u'%s' % (self.pregunta)
