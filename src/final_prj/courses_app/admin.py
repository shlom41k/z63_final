from django.contrib import admin

from .models import SchoolCourse, SchoolCourseDescriptionField, SchoolCourseApplication


@admin.register(SchoolCourse)
class SchoolCourseAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "number_of_lessons", ]
    prepopulated_fields = {"slug": ("name",), }


@admin.register(SchoolCourseDescriptionField)
class SchoolCourseDescriptionFieldAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "course", ]


@admin.register(SchoolCourseApplication)
class SchoolCourseApplicationFieldAdmin(admin.ModelAdmin):
    list_display = ["user_name", "course", "phone", "telegram", "status", ]
    list_editable = ["status", ]
    list_filter = ["status", ]
