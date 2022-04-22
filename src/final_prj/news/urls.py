# my_auth.urls file

from django.urls import path
from .views import MainView, PostDetailView, NewsSearchResultsView, NewsTagView, \
    NewsCreateView, NewsEditView, NewsDeleteView


urlpatterns = [
    path('', MainView.as_view(), name="news_index"),
    path('search/', NewsSearchResultsView.as_view(), name="news_search_results"),
    path('add_news/', NewsCreateView.as_view(), name="add_news"),
    path('edit_news/<slug>/', NewsEditView.as_view(), name="edit_news"),
    path('delete_news/<slug>/', NewsDeleteView.as_view(), name="delete_news"),
    path('<slug>/', PostDetailView.as_view(), name="news_detail"),
    path('tag/<slug:slug>/', NewsTagView.as_view(), name="news_tag"),
]

