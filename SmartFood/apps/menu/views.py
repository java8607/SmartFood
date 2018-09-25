from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse

# Create your views here.

class MenuHomePageView(TemplateView):
	
	def get(self, request, **kwargs):
		return render(request, 'menu.html', context=None)

class MenuPage(TemplateView):

	def get(self, request, **kwargs):
		return JsonResponse({
		    'ip': "foo",
		    'country': "bar"
		})
