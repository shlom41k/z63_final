# users_app.urls file

from django.urls import path
from .views import UserMainView


urlpatterns = [
    # User main page
    path("user/<user_name>/", UserMainView.as_view(), name="main_user"),
]


