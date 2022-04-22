from django.shortcuts import render
from django.views import View

from news.models import Post
from courses_app.models import SchoolCourse


class IndexView(View):
    """
    # Return home page
    """
    def get(self, request, *args, **kwargs):

        last_posts = Post.objects.filter(status=Post.PUBLISHED).order_by("-date_of_creating")[:4]
        last_courses = SchoolCourse.objects.all().order_by("-id")[:4]

        return render(request, "templates/main_home.html", context={
            "posts": last_posts,
            "courses": last_courses,
        })
