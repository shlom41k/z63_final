from django.contrib import admin

from .models import Course, Module, Lesson, Theme


# Admin panel for Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "course_status", "creator", "date_of_creating"]


# Admin panel for Module model
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ["order", "name", "course"]

    @admin.display(description="Number of modules in the course")
    def number_of_modules(self, obj: Module):
        return obj.course.module_set.count()


# Admin panel for Lesson model
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["order", "name", "module"]


# Admin panel for Theme model
@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ["order", "name", "lesson"]


