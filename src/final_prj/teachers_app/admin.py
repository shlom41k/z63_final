from django.contrib import admin

from .models import Teacher, TeacherContactInfo


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]
    prepopulated_fields = {"slug": ("first_name", "last_name")}


@admin.register(TeacherContactInfo)
class TeacherContactInfoAdmin(admin.ModelAdmin):
    list_display = ["teacher", "email"]
