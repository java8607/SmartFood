from django.urls import path
from apps.user import views

urlpatterns = [
	path('', views.UserHomePageView.as_view()),
	path('/new', views.UserHomePageView.as_view()),
]
