from django.db.models.functions import Sign
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View

from .forms import SigUpForm, MySigUpForm, SignInForm


class IndexView(View):
    """
    # Return home page
    """
    def get(self, request, *args, **kwargs):
        return render(request, "templates/base.html")


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
                return HttpResponseRedirect('/')

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
