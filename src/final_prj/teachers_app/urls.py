# teachers_app.urls file

from django.urls import path

from .views import TeachersView, TeacherDetailView


urlpatterns = [
    path("", TeachersView.as_view(), name="teachers"),
    path("<slug>/", TeacherDetailView.as_view(), name="teacher_detail"),
]


