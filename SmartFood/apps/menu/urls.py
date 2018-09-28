from django.urls import path
from apps.menu import views

urlpatterns = [
	path('', views.MenuHomePageView.as_view()),
	path('/new', views.MenuCreatePageView.as_view(), name='menu-create'),

]
