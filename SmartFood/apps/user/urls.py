from django.urls import path
from apps.user.views import UserHomePageView

userHomePageView = UserHomePageView()

urlpatterns = [
	path('', userHomePageView.get),
	path('/login', userHomePageView.login, name="login"),
]
