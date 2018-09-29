from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core import serializers
from django.http import JsonResponse, HttpResponse


from apps.preferences.form import PreferenceForm
from apps.diner.models import Preference


# Create your views here.
class PreferenceHomePageView(TemplateView):

	def preference_list(self, request, **kwargs):
		preference = Preference.objects.all()
		data = serializers.serialize("json", preference)			
		return JsonResponse(data, safe=False)
		
	def create(self, request, **kwargs):
		if request.method == "POST":
			favouriteType = request.POST.get('favouriteTypeOfProduct')
			#isGlutton = request.POST.get('isGlutton')
			print(request.POST)
			Preference.objects.create(favouriteTypeOfProduct=favouriteType, isGlutton = True)
		else:
			print("No entro al POST")
		
		return render(request, 'preferences.html', context=None)
		
	def get(self, request, **kwargs):
		return render(request, 'preferences.html', context=None)
