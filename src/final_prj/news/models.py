from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from pytils.translit import slugify
# from django.utils.text import slugify


class Post(models.Model):
    """
    # Class for news posts
    """
    header_h1 = models.CharField(verbose_name="Header", max_length=200)
    title = models.CharField(verbose_name="Title", max_length=200)
    slug = models.SlugField(verbose_name="Slug", blank=True, unique=True)
    description = RichTextUploadingField(verbose_name="Description")
    content = RichTextUploadingField(verbose_name="Content")
    image = models.ImageField(verbose_name="Image", blank=False)
    date_of_creating = models.DateField(verbose_name="Date of creating", default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag = TaggableManager()

    # Post status
    CREATED = "Created"
    REVIEW = "Review"
    PUBLISHED = "Published"
    REJECTED = "Rejected"

    POST_STATUSES = [
        (CREATED, "Created"),
        (REVIEW, "Review"),
        (PUBLISHED, "Published"),
        (REJECTED, "Rejected"),
    ]
    status = models.CharField(verbose_name="Status", max_length=10, choices=POST_STATUSES, default=CREATED)

    class Meta:
        ordering = ['-date_of_creating']

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return self.__str__()

    # Create slug for post
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.header_h1}")
        super(self.__class__, self).save(*args, **kwargs)

    # Get absolute url for post
    def get_url(self):
        return reverse("news_detail", args=[self.slug])


class Comment(models.Model):
    """
    # Class for comments
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(verbose_name="Comment")
    date_of_creating = models.DateTimeField(verbose_name="Date of creating", default=timezone.now)

    class Meta:
        ordering = ["-date_of_creating"]

    def __str__(self):
        return f"{self.author} - {self.text}"

    def __repr__(self):
        return self.__str__()


class CommentAnswer(models.Model):
    """
    # Class for answers to comments
    """
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="answers")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_answers")
    text = models.TextField(verbose_name="Answer")
    date_of_creating = models.DateTimeField(verbose_name="Date of creating", default=timezone.now)

    class Meta:
        ordering = ["date_of_creating"]

    def __str__(self):
        return f"{self.author} - {self.text}"

    def __repr__(self):
        return self.__str__()
