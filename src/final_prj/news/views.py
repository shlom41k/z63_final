from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator

from taggit.models import Tag

from .models import Post, Comment
from .forms import CommentForm, CommentAnswerForm, PostCreateForm


class MainView(View):
    """
    # Return home page
    """
    def get(self, request, *args, **kwargs):
        # Get posts, that are ready for public
        news = Post.objects.filter(status=Post.PUBLISHED)

        # Paginate news
        paginator = Paginator(news, 6)
        page_num = request.GET.get("page")
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
        last_posts = Post.objects.filter(status=Post.PUBLISHED).order_by("-date_of_creating")[:5]

        # Form for comments
        comment_form = CommentForm()
        comment_answer_form = CommentAnswerForm()

        return render(request, "news/post_detail.html", context={
            "post": post,
            "last_posts": last_posts,
            "form": comment_form,
            "answer_form": comment_answer_form,
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
            results = Post.objects.filter(status=Post.PUBLISHED).filter(Q(header_h1__icontains=query) |
                                                                        Q(content__icontains=query))

        # Paginate
        paginator = Paginator(results, 6)
        page_num = request.GET.get("page")
        page_obj = paginator.get_page(page_num)

        return render(request, "news/search_results.html", context={
            "title": "Поиск",
            "results": page_obj,
            "count": paginator.count,
        })


class NewsTagView(View):
    """
    # Return tag page
    """
    def get(self, request, slug, *args, **kwargs):
        # Get tag by slug
        tag = get_object_or_404(Tag, slug=slug)

        # Get posts by tag
        posts = Post.objects.filter(status=Post.PUBLISHED).filter(tag=tag)
        common_tags = Post.tag.most_common()

        # Paginate
        # paginator = Paginator(posts, 6)
        # page_num = request.GET.get("page")
        # page_obj = paginator.get_page(page_num)

        return render(request, "news/news_tag.html", context={
            "title": f"#ТЕГ {tag}",
            "posts": posts,
            "common_tags": common_tags,
        })


class NewsCreateView(View):
    """
    # Return create news page
    """
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()

        return render(request, "news/news_create.html", context={
            "form": form,
        })

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=True)
            post.author = request.user
            post.save()
            return redirect("user_profile")

        return render(request, "news/news_create.html", context={
            "form": form,
        })


class NewsEditView(View):
    """
    # Return edit news page
    """
    @method_decorator(login_required)
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.author == request.user and post.status == Post.REJECTED:
            form = PostCreateForm(instance=post)
            return render(request, "news/news_edit.html", context={"form": form, "post": post})
        else:
            messages.error(request, "Вы не можете редактировать эту запись")
            return redirect("user_posts")

    @method_decorator(login_required)
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.author == request.user and post.status == Post.REJECTED:
            form = PostCreateForm(request.POST, request.FILES, instance=post)

            if form.is_valid():
                post = form.save(commit=True)
                post.status = Post.CREATED
                post.save()
                messages.success(request, "Выбранная Вами записы была обновлена")
                return redirect("user_posts")

            messages.warning(request, "Пожалуйста, проверьте введенные данные")
            return render(request, "news/news_edit.html", context={
                "form": form,
                "post": post,
            })
        else:
            messages.error(request, "Вы не можете редактировать эту запись")
            return redirect("user_posts")


class NewsDeleteView(View):
    """
    # Return delete news page
    """
    @method_decorator(login_required)
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.author == request.user and post.status == Post.REJECTED:
            post.delete()
            messages.success(request, "Выбранная Вами записы была успешно удалена")
        else:
            messages.error(request, "Вы не можете удалить эту запись")

        return redirect("user_posts")
