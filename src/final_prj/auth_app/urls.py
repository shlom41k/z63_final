# my_auth.urls file

from django.urls import path

from .views import index


urlpatterns = [
    path('', index, name="index"),
]
