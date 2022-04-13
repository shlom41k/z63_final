# study_courses_app.urls file

from django.urls import path

from .views import CoursesView


urlpatterns = [
    path("", CoursesView.as_view(), name="study_courses"),
]


