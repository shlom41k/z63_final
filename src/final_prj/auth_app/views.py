from django.db.models.functions import Sign
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from .forms import SigUpForm, MySigUpForm, SignInForm, UserProfileForm, ProfileForm
from study_courses_app.models import Course


# class IndexView(View):
#     """
#     # Return home page
#     """
#     def get(self, request, *args, **kwargs):
#         return render(request, "templates/main_home.html")


class SignUpView(View):
    """
    # User registration
    """
    def get(self, request, *args, **kwargs):
        form = MySigUpForm()
        # form = UserCreationForm()
        return render(request, "auth_app/signup.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = MySigUpForm(request.POST)
        # form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            if user is not None:
                login(request, user)
                return redirect("add_profile")

        return render(request, "auth_app/signup.html", context={"form": form})


class SignInView(View):
    """
    # User sign in
    """
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, "auth_app/signin.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)

        if form.is_valid():

            user = authenticate(request, **form.cleaned_data)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')

        return render(request, "auth_app/signin.html", context={"form": form})


class AddProfileView(View):
    """
    # Add profile
    """

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user_form = UserProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

        return render(request, "auth_app/add_profile_info.html", context={
            "user_form": user_form,
            "profile_form": profile_form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        user_form = UserProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, _('Your profile was successfully updated!'))

            return HttpResponseRedirect("/")

        return render(request, "auth_app/add_profile_info.html", context={
            "user_form": user_form,
            "profile_form": profile_form})


class UserProfileView(View):
    """
    # User profile
    """
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        # Active courses
        user_courses = request.user.current_courses.all().order_by("-date_of_creating")[:5]
        user_posts = request.user.posts.all().order_by("-date_of_creating")[:5]

        return render(request, "auth_app/profile.html", context={
            "user_courses": user_courses,
            "user_posts": user_posts,
        })

