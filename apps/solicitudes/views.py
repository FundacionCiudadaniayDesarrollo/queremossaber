# -*- coding: utf-8 -*-
##########################################################################
####     Copyright 2014 CMAGINET -  Todos los Derechos reservados     ####
####                       www.cmaginet.com                           ####
#### Se prohibe la divulgación, utilización, transmisión,             ####
#### distribución, reproducción y transformación, total o parcial,    ####
#### en cualquier soporte o medio, de los contenidos de este software ####
#### sin previa autorización de CMAGINET.                             ####
##########################################################################
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from json import dumps
from django.db.models import Count
from django.contrib import auth

from twitter import Api as twitterApi

from .emails import crearPregunta, seguirPregunta
from vanilla import TemplateView, ListView, DetailView

import requests

#MODELOS
from .models import preguntaTemporal, Categoria, Solicitud
from django.contrib.auth.models import User


domain = 'https://queremossaber.ec'

class preguntaTemporalProcesarView(TemplateView):
	template_name = 'frontend/home/index.html'
	resultado     = False

	def get(self, request, *args, **kwargs):
		token = kwargs['token']
		if(preguntaTemporal.objects.filter(token=token).count()>0):
			pregunta  = preguntaTemporal.objects.get(token=token)
			
			if(Solicitud.objects.filter(token=token).count()==0):
				solicitud = Solicitud(\
								pregunta    = pregunta.pregunta,
								institucion = pregunta.institucion,
								token       = pregunta.token,
								usuario     = request.user,
							)
				solicitud.save()
				solicitud.seguidores.add( solicitud.usuario )

				## PUBLICAR TWEET
				publishTweet(self.request.user, solicitud.slug, True)
				
				## ENVIAR EMAIL
				#crearPregunta(self.request.user, solicitud)

				## PUBLICAR FACEBOOK
				publishFacebook(self.request.user, solicitud.slug)				

			self.resultado = True
		else:
			self.resultado = False
		return super(preguntaTemporalProcesarView, self).get(self, request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context          = super(preguntaTemporalProcesarView, self).get_context_data(**kwargs)	
		context['resultado'] = self.resultado
		context['destacadas'] = Solicitud.objects.annotate(num_seguidores=Count('seguidores')).order_by('-num_seguidores')[:3]
		context['categorias'] = Categoria.objects.all()		
		return context

class solicitudesListView(ListView):
	template_name = 'frontend/solicitudes/listview.html'
	model         = Solicitud
	paginate_by   = 20
	page_kwarg    = 'pagina'
	categoria     = ''
	buscar        = ''

	def get(self, request, *args, **kwargs):
		if ('categoria' in kwargs) :
			self.categoria = kwargs['categoria']
		if ('buscar' in kwargs):
			self.buscar = kwargs['buscar']
		return super(solicitudesListView, self).get(self, request, *args, **kwargs)	

	def get_queryset(self):
		if self.categoria:
			categoria = get_object_or_404(Categoria, slug=self.categoria)
			queryset = self.model.objects.filter(categoria=categoria, publicado=True).order_by('-fecha')
		elif self.buscar:
			queryset = self.model.objects.filter(pregunta__icontains=self.buscar, publicado=True).order_by('-fecha')
		else:
			queryset = self.model.objects.filter(publicado=True).order_by('-fecha')
		return queryset

	def get_context_data(self, **kwargs):
		context               = super(solicitudesListView, self).get_context_data(**kwargs)	
		context['buscar']     = self.buscar
		context['categoria']  = self.categoria
		context['categorias'] = Categoria.objects.all()
		return context

class solicitudesDetailView(DetailView):
	template_name    = 'frontend/solicitudes/detailview.html'
	model            = Solicitud
	lookup_field     = 'slug'
	lookup_url_kwarg = 'slug'
	token            = ''

	def get(self, request, *args, **kwargs):
		if('token' in kwargs and self.request.user) :
			self.token = kwargs['token']
			self.get_object().seguidores.add( self.request.user )

			## PUBLICAR TWEET
			publishTweet(self.request.user, self.get_object().slug, False)

			## ENVIAR EMAIL
			seguirPregunta(self.request.user, self.get_object())

			## PUBLICAR FACEBOOK
			publishFacebook(self.request.user, self.get_object().slug)

		return super(solicitudesDetailView, self).get(self, request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context                = super(solicitudesDetailView, self).get_context_data(**kwargs)
		context['title']       = 'Hice una pregunta a: %s' % self.get_object().institucion
		context['description'] = self.get_object().pregunta
		context['image']       = '%s/static/img/queremossaber-1200x630.jpg' % domain
		context['url']         = '%s%s' % (domain, reverse('solicitudes-detalle', args=[self.get_object().slug]))
		context['categorias']  = Categoria.objects.all()

		if( self.token ):
			context['seguimiento'] = True

		return context

## PUBLICAR TWEET
def publishTweet(user, slug, creado):
	if( user.social_auth.filter(provider='twitter').count()>0 ):
		oauth   = user.social_auth.get(provider='twitter').extra_data['access_token']
		otoken  = oauth['oauth_token']
		osecret = oauth['oauth_token_secret']
		twitter = twitterApi(consumer_key='MxZRgHhcYF9rRo8CSENrYEGVi', consumer_secret='qVeprVclXIjuzH4DSB1T9XPd3kGOaF2y7HXABWv4jqES05FzrH', access_token_key=otoken, access_token_secret=osecret)
		url		= '%s%s' % ( domain, reverse( 'solicitudes-detalle', args=[slug] ) )

		if( creado ):
			twitter.PostUpdate('He solicitado información vía @QueremosSaberEC. Revisa mi pregunta aquí: %s' % url)
		else:			
			twitter.PostUpdate('Estoy siguiendo una pregunta vía @QueremosSaberEc. Revisa la misma aquí: %s' % url)	


#PUBLICAR EN FACEBOOK
def publishFacebook(user, slug):
	if hasattr(user, 'social_auth'):
		if user.social_auth.filter(provider='facebook').count()>0:
			socialuser  = user.social_auth.get(provider='facebook')
			if hasattr(socialuser, 'uid'):
				uid        = socialuser.uid
				token      = socialuser.extra_data['access_token']
				url        = '%s%s' % ( domain, reverse( 'solicitudes-detalle', args=[slug] ) )
				urlrequest = 'https://graph.facebook.com/%s/feed?link=%s&access_token=%s' % (uid, url, token)
				result     = requests.post(urlrequest)
				result_log  = open('log_facebook.log','w')
				result_log.write( urlrequest.encode('utf-8') )#str(result).encode('utf-8') )
				result_log.close()

## LOGUEAR USUARIO POR FORMULARIO ##
def loguearUsuarioEmail(request, slug):
	if request.is_ajax():
		if( request.method == 'POST' ):
			nombre = request.POST.getlist('nombre')[0]
			email  = request.POST.getlist('email')[0]
			token  = slug

			if(User.objects.filter(email=email).count()==0):
				usuario = User.objects.create_user(
					username=email,
					email=email,
					password=email
				)

				usuario.first_name = nombre
				usuario.save()

				user = auth.authenticate(username=email, password=email)
				if user is not None:
					if user.is_active:
						auth.login(request, user)

			else:
				user = auth.authenticate(username=email, password=email)
				if user is not None:
					if user.is_active:
						auth.login(request, user)

			context = dumps({'token': str(token)})
			return HttpResponse(context, content_type='application/json')	

	if( request.method == 'POST' ):
		nombre   = request.POST.getlist('nombre')[0]
		apellido = request.POST.getlist('apellido')[0]
		email    = request.POST.getlist('email')[0]

		if(User.objects.filter(email=email).count()==0):
			usuario = User.objects.create_user(
				username=email,
				email=email,
				password=email
			)

			usuario.first_name = nombre
			usuario.last_name  = apellido
			usuario.save()

			user = auth.authenticate(username=email, password=email)
			if user is not None:
				if user.is_active:
					auth.login(request, user)

		else:
			user = auth.authenticate(username=email, password=email)
			if user is not None:
				if user.is_active:
					auth.login(request, user)

	solicitud = Solicitud.objects.get(slug=slug)

	return HttpResponseRedirect( reverse('solicitudes-detalle-token', args=[solicitud.slug, solicitud.token]) )

## AJAX ##
def preguntaTemporalGuardarView(request):
	data = []
	if request.is_ajax():
		if request.method=='POST':
			if (request.POST.getlist('pregunta')):
				pregunta    = request.POST.getlist('pregunta')[0]
				institucion = request.POST.getlist('institucion')[0]

				pregunta    = preguntaTemporal(pregunta=pregunta, institucion=institucion)

				pregunta.save()				
				data = str(pregunta.token)

	context = dumps({'token': data})
	return HttpResponse(context, content_type='application/json')	