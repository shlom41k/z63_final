from django.contrib import admin
from .models import Post, Comment, CommentAnswer


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["header_h1", "title"]
    prepopulated_fields = {"slug": ("header_h1",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["text", "post", "author", "date_of_creating"]


@admin.register(CommentAnswer)
class CommentAnswerAdmin(admin.ModelAdmin):
    list_display = ["text", "comment", "author", "date_of_creating"]
