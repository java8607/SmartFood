from django.shortcuts import render
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
				return render(request, 'maker.html', context=None)
			else:				
				return JsonResponse('error: Usuario o clave invalidos', safe=False)	
		else:
			print("No es  POST *****************************")		
		return render(request, 'index.html', context=None)