# my_auth.urls file

from django.urls import path
from .views import MainView, PostDetailView, NewsSearchResultsView, NewsTagView


urlpatterns = [
    path('', MainView.as_view(), name="news_index"),
    path('search/', NewsSearchResultsView.as_view(), name="news_search_results"),
    path('<slug>/', PostDetailView.as_view(), name="news_detail"),
    path('tag/<slug:slug>/', NewsTagView.as_view(), name="news_tag"),
]

