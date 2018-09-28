from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse

# Create your views here.

class MenuHomePageView(TemplateView):
	
	def get(self, request, **kwargs):
		return render(request, 'menu.html', context=None)

class MenuCreatePageView(TemplateView):

	def get(self, request, **kwargs):
		return render(request, 'menu.create.html', context=None)

class MenuPage(TemplateView):	

	def get(self, request, **kwargs):
		products = []

		products.append({
			    'id': 1,
			    'producto': "Frijoles"
			})
		products.append({
			    'id': 2,
			    'producto': "Mazamorra"
			})
		products.append({
			    'id': 3,
			    'producto': "Chicharron"
			})
		return JsonResponse(products, safe=False)

	def post(self, request, **kwargs):
		print('REQUEST CONSOLE: ', request)
		return HttpResponse('')
