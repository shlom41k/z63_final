# my_auth.urls file

from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings

from .views import IndexView, SignUpView, SignInView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signin/", SignInView.as_view(), name="signin"),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout',),
]


