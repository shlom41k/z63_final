from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    """
    # Return home page
    """
    def get(self, request, *args, **kwargs):
        return render(request, "templates/home.html")