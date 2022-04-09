# teachers_app.urls file

from django.urls import path

from .views import TeachersView, TeacherDetailView


urlpatterns = [
    path("", TeachersView.as_view(), name="teachers"),
    path("teacher/<int:teacher_id>", TeacherDetailView.as_view(), name="teacher_detail"),
]


