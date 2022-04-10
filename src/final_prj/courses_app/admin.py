from django.contrib import admin

from .models import SchoolCourse, SchoolCourseDescriptionField


@admin.register(SchoolCourse)
class SchoolCourseAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "number_of_lessons"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(SchoolCourseDescriptionField)
class SchoolCourseDescriptionFieldAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "course"]
