from django.shortcuts import render
from django.views import View


class CoursesView(View):
    """
    Returns a list of Courses
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'courses_app/courses.html', context={"title": "Выберите подходящий для Вас курс",
                                                                    "num": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
