from django.urls import path
from apps.user.views import UserHomePageView

userHomePageView = UserHomePageView()

urlpatterns = [
	path('', userHomePageView.login),
	path('/login', userHomePageView.login, name="login"),
]
