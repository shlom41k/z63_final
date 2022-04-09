from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Teacher


class TeachersView(View):
    def get(self, request, *args, **kwargs):
        teachers = Teacher.objects.all()

        return render(request, 'teachers_app/teachers.html', context={"title": "Наши преподаватели", "teachers": teachers})


class TeacherDetailView(View):
    def get(self, request, teacher_id, *args, **kwargs):
        teacher = get_object_or_404(Teacher, id=teacher_id)

        return render(request, 'teachers_app/teacher_detail.html', context={"title": "Преподаватель", "teacher": teacher})