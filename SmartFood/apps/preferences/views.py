from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class MenuHomePageView(TemplateView):
	
	def get(self, request, **kwargs):
		return render(request, 'preferences.html', context=None)