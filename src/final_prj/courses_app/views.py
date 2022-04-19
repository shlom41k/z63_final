from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from django.views import View
from .models import SchoolCourse
from .forms import SchoolCourseApplicationForm


class SchoolCoursesView(View):
    """
    Returns a list of Courses
    """
    def get(self, request, *args, **kwargs):
        school_courses = SchoolCourse.objects.all()

        return render(request, "courses_app/courses.html", context={"title": "Выберите подходящий для Вас курс",
                                                                    "courses": school_courses})


class SchoolCourseDetailView(View):
    """
    Returns a detail of a SchoolCourse
    """
    def get(self, request, slug, *args, **kwargs):
        school_course = get_object_or_404(SchoolCourse, slug=slug)

        form = SchoolCourseApplicationForm(initial={"course": school_course})

        return render(request, "courses_app/school_course_detail.html", context={"title": school_course.name,
                                                                                 "course": school_course,
                                                                                 "form": form,
                                                                                 })

    def post(self, request, slug, *args, **kwargs):
        school_course = get_object_or_404(SchoolCourse, slug=slug)

        form = SchoolCourseApplicationForm(request.POST)
        print(form.data)

        if form.is_valid():
            form.save()
            messages.success(request, "Ваша заявка отправлена")
            print("Saved")

        # return render(request, "courses_app/school_course_detail.html", context={"title": school_course.name,
        #                                                                          "course": school_course,
        #                                                                          "form": form,
        #                                                                          })
        return redirect("school_course_detail", slug=slug)
