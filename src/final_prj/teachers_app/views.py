from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages

from .models import Teacher
from .forms import IndividualLessonApplicationForm


class TeachersView(View):
    """
    View for teachers page
    """
    def get(self, request, *args, **kwargs):
        teachers = Teacher.objects.all()

        return render(request, 'teachers_app/teachers.html', context={
            "title": "Наши преподаватели",
            "teachers": teachers,
        })


class TeacherDetailView(View):
    """
    View for teacher detail page
    """
    def get(self, request, slug, *args, **kwargs):
        teacher = get_object_or_404(Teacher, slug=slug)

        form = IndividualLessonApplicationForm(initial={"teacher": teacher, })

        return render(request, 'teachers_app/teacher_detail.html', context={
            "title": "Преподаватель",
            "teacher": teacher,
            "form": form,
        })

    # Getting application for individual lesson
    def post(self, request, slug, *args, **kwargs):
        teacher = get_object_or_404(Teacher, slug=slug)

        form = IndividualLessonApplicationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Ваша заявка успешно отправлена")

        return redirect("teacher_detail", slug=slug)
