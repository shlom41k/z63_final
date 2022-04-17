from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Course, Module, Lesson, Theme


class CoursesView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()

        # Paginate courses
        paginator = Paginator(courses, 6)

        # Get page number from url
        page_num = request.GET.get("page", 1)

        # Get page object
        page_obj = paginator.get_page(page_num)

        return render(request, "study_courses_app/study_courses.html", context={
            "title": "Курсы для самообучения",
            "page_obj": page_obj,
        })


class CourseDetailView(View):
    @method_decorator(login_required)
    def get(self, request, course_id, *args, **kwargs):

        course = get_object_or_404(Course, pk=course_id)

        return render(request, "study_courses_app/study_course_detail.html", context={
            "title": f"{course.name}",
            "course": course,
        })


class StudyCourseView(View):
    @method_decorator(login_required)
    def get(self, request, course_id, module_id=1, lesson_id=1, theme_id=1, *args, **kwargs):

        course = get_object_or_404(Course, pk=course_id)
        module = course.modules.get(order=module_id)
        lesson = module.lessons.get(order=lesson_id)
        theme = lesson.themes.get(order=theme_id)

        return render(request, "study_courses_app/study_course.html", context={
            "title": f"{course.name}",
            "course": course,
            "module": module,
            "lesson": lesson,
            "theme": theme,
        })
