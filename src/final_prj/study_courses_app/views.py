from django.shortcuts import render, get_object_or_404, redirect
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
        paginator = Paginator(courses, 8)

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

        if course.course_status != Course.COMPLETED:
            return redirect("study_course_detail", course_id=course_id)

        module = course.modules.get(order=module_id)
        lesson = module.lessons.get(order=lesson_id)
        theme = lesson.themes.get(order=theme_id)

        if (request.user not in course.students.all()) and (request.user not in course.old_students.all()):
            # print("Add user to course")
            course.students.add(request.user)

        return render(request, "study_courses_app/study_course.html", context={
            "title": f"{course.name}",
            "course": course,
            "module": module,
            "current_lesson": lesson,
            "theme": theme,
        })


class StudyCourseToArchiveView(View):
    @method_decorator(login_required)
    def get(self, request, course_id, *args, **kwargs):

        course = get_object_or_404(Course, pk=course_id)

        if request.user in course.students.all():
            course.students.remove(request.user)

        if request.user not in course.old_students.all():
            course.old_students.add(request.user)

        return redirect("study_course_detail", course_id=course_id)
