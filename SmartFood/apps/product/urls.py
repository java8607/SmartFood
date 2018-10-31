from django.urls import path
from apps.product import views

urlpatterns = [
	path('', views.ProductHomePageView.as_view(), name="product"),
	path('/new', views.ProductHomePageView.new, name="new-product"),
	path('/all', views.ProductHomePageView.getAll),
	path('/ingredients/all', views.IngredientPageView.getAll),
	


]
