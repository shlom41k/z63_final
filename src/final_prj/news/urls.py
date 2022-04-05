# my_auth.urls file

from django.urls import path
from .views import MainView


urlpatterns = [
    path('', MainView.as_view(), name="news_index"),
]

