# teachers_app.urls file

from django.urls import path

from .views import TeachersView


urlpatterns = [
    path("", TeachersView.as_view(), name="teachers"),
]


