from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from django.views import View


class UserMainView(View):
    """
    View for some user main page
    """
    @method_decorator(login_required)
    def get(self, request, user_name, *args, **kwargs):

        some_user = get_object_or_404(User, username=user_name)

        if some_user == request.user:
            return redirect("user_profile")

        # Last N user posts
        some_user_posts = some_user.posts.all().order_by("-date_of_creating")[:5]

        return render(request, "users_app/user_main.html", context={
            "some_user": some_user,
            "some_user_posts": some_user_posts,
        })
