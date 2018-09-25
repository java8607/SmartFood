from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class RestaurantHomePageView(TemplateView):
	
	def get(self, request, **kwargs):
		return render(request, 'restaurant.html', context=None)