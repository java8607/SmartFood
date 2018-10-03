from django.urls import path
from apps.makerDecision.views import MakerHomePageView

makerHomePageView = MakerHomePageView()

urlpatterns = [
	path('/search', makerHomePageView.searchProduct, name="search"),
]
