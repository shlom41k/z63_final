# users_app.urls file

from django.urls import path
from .views import UserMainView, SomeUserPostsView


urlpatterns = [
    # User main page
    path("user/<user_name>/", UserMainView.as_view(), name="main_user"),
    path("user/<user_name>/posts/", SomeUserPostsView.as_view(), name="some_user_posts"),
]


