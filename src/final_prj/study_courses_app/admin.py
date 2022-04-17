from django.contrib import admin
from .models import Course, Module, Lesson, Theme


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "course_status", "creator", "date_of_creating"]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ["order", "name", "course"]

    @admin.display(description="Number of modules in the course")
    def number_of_modules(self, obj: Module):
        return obj.course.module_set.count()


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["order", "name", "module"]


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ["order", "name", "lesson"]


