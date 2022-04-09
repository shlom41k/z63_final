from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q

from taggit.models import Tag

from .models import Post, Comment
from .forms import CommentForm


class MainView(View):
    """
    # Return home page
    """
    def get(self, request, *args, **kwargs):
        news = Post.objects.all()

        # Paginate news
        paginator = Paginator(news, 6)

        # Get page number from url
        page_num = request.GET.get("page")

        # Get page object
        page_obj = paginator.get_page(page_num)

        return render(request, "news/home.html", context={"page_obj": page_obj})


class PostDetailView(View):
    """
    # Return post detail page
    """
    def get(self, request, slug, *args, **kwargs):
        # Get post by slug
        post = get_object_or_404(Post, slug=slug)

        # Get last 5 posts
        last_posts = Post.objects.all().order_by("-id")[:5]

        # Form for comments
        comment_form = CommentForm()

        return render(request, "news/post_detail.html", context={
            "post": post,
            "last_posts": last_posts,
            "form": comment_form,
        })

    def post(self, request, slug, *args, **kwargs):

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            text = request.POST.get("text")
            user = request.user
            post = get_object_or_404(Post, slug=slug)
            comment = Comment.objects.create(post=post, author=user, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        return render(request, 'news/post_detail.html', context={'comment_form': comment_form})


class NewsSearchResultsView(View):
    """
    # Return search results page
    """
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        results = ""

        # Search by title and content
        if query:
            results = Post.objects.filter(Q(header_h1__icontains=query) | Q(content__icontains=query))

        # Paginate
        paginator = Paginator(results, 6)
        page_num = request.GET.get("page")
        page_obj = paginator.get_page(page_num)

        return render(request, "news/search_results.html", context={"title": "Поиск", "results": page_obj, "count": paginator.count})


class NewsTagView(View):
    """
    # Return tag page
    """
    def get(self, request, slug, *args, **kwargs):
        # Get tag by slug
        tag = get_object_or_404(Tag, slug=slug)

        # Get posts by tag
        posts = Post.objects.filter(tag=tag)
        common_tags = Post.tag.most_common()

        # # Paginate
        # paginator = Paginator(posts, 6)
        # page_num = request.GET.get("page")
        # page_obj = paginator.get_page(page_num)

        return render(request, "news/news_tag.html", context={"title": f"#ТЕГ {tag}", "posts": posts, "common_tags": common_tags})