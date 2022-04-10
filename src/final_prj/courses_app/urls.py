# courses_app.urls file

from django.urls import path
from .views import SchoolCoursesView, SchoolCourseDetailView


urlpatterns = [
    path("", SchoolCoursesView.as_view(), name="school_courses"),
    path("<slug>/", SchoolCourseDetailView.as_view(), name="school_course_detail"),
]


