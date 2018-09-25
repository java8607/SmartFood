from django.urls import path
from menu import views

urlpatterns = [
	path('', views.MenuHomePageView.as_view()),
	path('/api', views.MenuPage.as_view()),

]
