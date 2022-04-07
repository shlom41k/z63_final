from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator

from .models import Post


class MainView(View):
    """
    # Return home page
    """
    def get(self, request, *args, **kwargs):
        news = Post.objects.all()

        # Paginate posts
        paginatior = Paginator(news, 6)

        # Get page number from url
        page_num = request.GET.get('page')

        # Get page object
        page_obj = paginatior.get_page(page_num)

        return render(request, "news/home.html", context={"page_obj": page_obj})


class PostDetailView(View):
    """
    # Return post detail page
    """
    def get(self, request, slug, *args, **kwargs):
        # Get post by slug
        post = get_object_or_404(Post, slug=slug)

        return render(request, "news/post_detail.html", context={"post": post})
