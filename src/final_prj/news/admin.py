from django.contrib import admin
from .models import Post, Comment, CommentAnswer


# Admin panel for Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["header_h1", "author", "date_of_creating", "status", ]
    list_filter = ["status", ]
    list_editable = ["status", ]
    prepopulated_fields = {"slug": ("header_h1",), }


# Admin panel for Comment model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["text", "post", "author", "date_of_creating", ]


# Admin panel for CommentAnswer model
@admin.register(CommentAnswer)
class CommentAnswerAdmin(admin.ModelAdmin):
    list_display = ["text", "comment", "author", "date_of_creating", ]
