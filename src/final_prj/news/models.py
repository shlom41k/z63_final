from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    """
    # Class for news posts
    """

    header_h1 = models.CharField(verbose_name="Header", max_length=200)
    title = models.CharField(verbose_name="Title", max_length=200)
    slug = models.SlugField(verbose_name="Slug")
    description = RichTextUploadingField(verbose_name="Description")
    content = RichTextUploadingField(verbose_name="Content")
    image = models.ImageField(verbose_name="Image")
    date_of_creating = models.DateField(verbose_name="Date of creating", default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tag = models.CharField(verbose_name="Tags", max_length=200)

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return self.__str__()
