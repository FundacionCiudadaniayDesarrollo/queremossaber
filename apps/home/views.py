# -*- coding: utf-8 -*-
##########################################################################
####     Copyright 2014 CMAGINET -  Todos los Derechos reservados     ####
####                       www.cmaginet.com                           ####
#### Se prohibe la divulgación, utilización, transmisión,             ####
#### distribución, reproducción y transformación, total o parcial,    ####
#### en cualquier soporte o medio, de los contenidos de este software ####
#### sin previa autorización de CMAGINET.                             ####
##########################################################################
from vanilla import TemplateView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect


from django.db.models import Count

#MODELOS
from apps.solicitudes.models import Categoria, Solicitud

class portalHome(TemplateView):
	template_name = 'frontend/home/index.html'

	def get_context_data(self, **kwargs):
		context               = super(portalHome, self).get_context_data(**kwargs)
		context['destacadas'] = Solicitud.objects.filter(publicado=True).annotate(num_seguidores=Count('seguidores')).order_by('-num_seguidores')[:3]
		context['categorias'] = Categoria.objects.all()
		return context

#Vistas estáticas
class portalIniciativa(TemplateView):
	template_name = 'frontend/home/iniciativa.html'

class portaltuDerecho(TemplateView):
	template_name = 'frontend/home/tu_derecho_saber.html'

class portalLotaip(TemplateView):
	template_name = 'frontend/home/lotaip.html'

class portalContact(TemplateView):
	template_name = 'frontend/home/contact.html'

	def post(self, request, *args, **kwargs):
		print request.POST.getlist('form-nombre')
		print request.POST.getlist('form-email')
		print request.POST.getlist('form-asunto')
		print request.POST.getlist('form-mensaje')

		return HttpResponseRedirect('/portal/contactenos/success/')

	def get_context_data(self, **kwargs):
		context                = super(portalContact, self).get_context_data(**kwargs)
		context['menu']        = 'contacto'
		context['description'] = '¿Quieres obtener más información de Decretazo, compartir una idea con nosotros o hacer un comentario? Envíanos un correo electrónico a info@decretazo.com o llena el formulario a continuación. <br/> Te responderemos tan pronto como sea posible.'
		context['keywords']    = 'Contáctenos'
		context['title']       = 'Contáctenos'
		return context

class portalContactResponse(TemplateView):
	template_name = 'frontend/home/contact_response.html'
	
	def get_context_data(self, **kwargs):
		context                = super(portalContactResponse, self).get_context_data(**kwargs)
		context['menu']        = 'contacto'
		context['description'] = '¿Quieres obtener más información de Decretazo, compartir una idea con nosotros o hacer un comentario? Envíanos un correo electrónico a info@decretazo.com o llena el formulario a continuación. <br/> Te responderemos tan pronto como sea posible.'
		context['keywords']    = 'Contáctenos'
		context['title']       = 'Contáctenos'
		return context

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')