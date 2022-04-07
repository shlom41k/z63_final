from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["header_h1", "title"]
    prepopulated_fields = {"slug": ("header_h1",)}
