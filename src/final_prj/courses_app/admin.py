from django.contrib import admin

from .models import SchoolCourse, SchoolCourseDescriptionField, SchoolCourseApplication


# Admin panel for SchoolCourse model
@admin.register(SchoolCourse)
class SchoolCourseAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "number_of_lessons", ]
    prepopulated_fields = {"slug": ("name",), }


# Admin panel for SchoolCourseDescriptionField model
@admin.register(SchoolCourseDescriptionField)
class SchoolCourseDescriptionFieldAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "course", ]


# Admin panel for SchoolCourseApplication model
@admin.register(SchoolCourseApplication)
class SchoolCourseApplicationFieldAdmin(admin.ModelAdmin):
    list_display = ["user_name", "course", "phone", "telegram", "status", ]
    list_editable = ["status", ]
    list_filter = ["status", ]
