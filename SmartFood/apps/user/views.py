from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.core import serializers
from apps.user.models import User
from django.http import JsonResponse
# Create your views here.

class UserHomePageView(TemplateView):
	
	def get(self, request, **kwargs):			
		return render(request, 'index.html', context=None)
	
	def login(self, request, **kwargs):
		if request.method == "POST":
			user = request.POST.get('usr')
			password = request.POST.get('psw')
			result = User.objects.get(userName = user)
			
			if result.password == password:	
				request.session['usr'] = user
				request.session['id'] = result.id							
				return render(request, 'maker.html', context=None)
			else:				
				return render_to_response("index.html", {'respuesta':'error: Usuario o clave invalidos'})		
		
		return render(request, 'index.html', context=None)