# -*- coding: utf-8 -*-
##########################################################################
####     Copyright 2014 CMAGINET -  Todos los Derechos reservados     ####
####                       www.cmaginet.com                           ####
#### Se prohibe la divulgación, utilización, transmisión,             ####
#### distribución, reproducción y transformación, total o parcial,    ####
#### en cualquier soporte o medio, de los contenidos de este software ####
#### sin previa autorización de CMAGINET.                             ####
##########################################################################
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import render


domain     = 'https://queremossaber.ec'
from_email = 'Queremos Saber <notificaciones@queremossaber.ec>'

def crearPregunta(user, solicitud): 
	if(user.email):
		title        = 'Pregunta'
		asunto       = 'Confirmación de pregunta en Queremos Saber'
		email        = u'%s <%s>' % (user.first_name, user.email)
		context      = {'title': title, 'domain': domain, 'nombre': '%s %s' % (user.first_name, user.last_name), 'solicitud': solicitud}
		html_content = render_to_string( 'emails/seguir_pregunta.html', context )
		msg          = EmailMultiAlternatives(asunto, title, from_email, [email])
		msg.attach_alternative(html_content, "text/html")
		msg.send()

		#ENVIAR CONFIRMACIÓN ADMINISTRADOR
		title  = 'Han realizado una nueva pregunta en Queremos Saber'
		asunto = 'Han realizado una nueva pregunta en Queremos Saber'
		email  = u'%s <%s>' % ('Queremos Saber', 'info@queremossaber.ec')
		msg    = EmailMultiAlternatives(asunto, title, from_email, [email])
		msg.attach_alternative(html_content, "text/html")
		msg.send()

def seguirPregunta(user, solicitud): 
	if(user.email):
		title        = 'Pregunta'
		asunto       = 'Confirmación de seguimiento a pregunta'
		email        = u'%s <%s>' % (user.first_name, user.email)
		context      = {'title': title, 'domain': domain, 'nombre': '%s %s' % (user.first_name, user.last_name), 'solicitud': solicitud}
		html_content = render_to_string( 'emails/seguir_pregunta.html', context )
		msg          = EmailMultiAlternatives(asunto, title, from_email, [email])
		msg.attach_alternative(html_content, "text/html")
		msg.send()

		# f = open('workfile.html', 'w')
		# f.write(html_content.encode('utf-8'))
		# f.close()