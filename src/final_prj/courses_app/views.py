from django.shortcuts import render, get_object_or_404

from django.views import View
from .models import SchoolCourse


class SchoolCoursesView(View):
    """
    Returns a list of Courses
    """
    def get(self, request, *args, **kwargs):
        school_courses = SchoolCourse.objects.all()

        return render(request, 'courses_app/courses.html', context={"title": "Выберите подходящий для Вас курс",
                                                                    "courses": school_courses})


class SchoolCourseDetailView(View):
    """
    Returns a detail of a SchoolCourse
    """
    def get(self, request, slug, *args, **kwargs):
        school_course = get_object_or_404(SchoolCourse, slug=slug)
        print("Here")

        return render(request, 'courses_app/school_course_detail.html', context={"title": school_course.name,
                                                                                 "course": school_course})