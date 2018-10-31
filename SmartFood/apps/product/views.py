from django.shortcuts import render
from django.views.generic import TemplateView
from django.core import serializers
from django.http import JsonResponse, HttpResponse

from apps.restaurant.models import Product, Ingredient

class ProductInterface:
	def get(self):
		return

	def getAll(self):
		return
				
	def new(self):
		return

class ProductHomePageView(ProductInterface,TemplateView):

	def get(self, request, **kwargs):
		return render(request, 'product.html', context=None)

	def getAll(request):
		return JsonResponse(
				serializers.serialize("json", Product.objects.all()),
				safe=False
			)

	def new(request):
		return render(request, 'product.create.html', context=None)

class IngredientPageView(TemplateView):

	def getAll(request):
		return JsonResponse(
				serializers.serialize("json", Ingredient.objects.all()),
				safe=False
			)