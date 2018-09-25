from django.urls import path
from apps.restaurant import views

urlpatterns = [
	path('', views.RestaurantHomePageView.as_view()),
]
