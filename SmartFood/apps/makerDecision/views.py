from django.shortcuts import render, redirect, render_to_response
from django.views.generic import TemplateView
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from apps.diner.models import Diner
from apps.diner.models import Preference
from apps.restaurant.models import Restaurant
from apps.restaurant.models import Product
from apps.restaurant.models import Menu


# Create your views here.
class MakerHomePageView(TemplateView):

	def searchProduct(self, request, **kwargs):
		user = request.session['usr']
		id = request.session['id']
		diner = self.getProfile(id)

		products = Product.objects.all()
		menus = Menu.objects.all()		
		preference = Preference.objects.all()					
		restaurant = Restaurant.objects.all()					
		
		productsElegibles = ''
		#menus = serializers.serialize("json", menus)	
		
		for prod in products:
				if diner.budget >= prod.price:
					productsElegibles += prod.name
					for menu in menus:
						print(menu)
						if menu.product == prod:						
							for rest in restaurants:
								if rest.menu == menu:
									print(rest.coordinates+"**********************")
					
		respuesta = str(diner.budget)+" COP, un producto ideal para tí sería "+productsElegibles
		print(respuesta)
		return render_to_response("maker.html", {'respuesta':respuesta})
		
	def getProfile(self, id):
		return Diner.objects.get(user_id = id)					
		
