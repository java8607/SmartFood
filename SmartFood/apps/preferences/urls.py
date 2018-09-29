from django.urls import path
from django.conf.urls import url
from apps.preferences.views import PreferenceHomePageView

preferenceHomePageView = PreferenceHomePageView()

urlpatterns = [
	path('/list', preferenceHomePageView.preference_list, name='preference-list'),
	path('/get', preferenceHomePageView.get, name='preference-get'),
	path('/new', preferenceHomePageView.create, name='preference-create'),

]

