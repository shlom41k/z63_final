# study_courses_app.urls file

from django.urls import path

from .views import CoursesView, CourseDetailView, StudyCourseView


urlpatterns = [
    path("", CoursesView.as_view(), name="study_courses"),
    path("<int:course_id>", CourseDetailView.as_view(), name="study_course_detail"),
    path("study/<int:course_id>/<int:module_id>/<int:lesson_id>/<int:theme_id>", StudyCourseView.as_view(), name="study_course"),
]


