# my_auth.urls file

from django.urls import path
from .views import MainView, PostDetailView


urlpatterns = [
    path('', MainView.as_view(), name="news_index"),
    path('<slug>/', PostDetailView.as_view(), name="news_detail"),
]

