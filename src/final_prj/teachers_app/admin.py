from django.contrib import admin

from .models import Teacher, TeacherContactInfo, IndividualLessonApplication


# Admin panel for teachers
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]
    prepopulated_fields = {"slug": ("first_name", "last_name")}


# Admin panel for teachers contact info
@admin.register(TeacherContactInfo)
class TeacherContactInfoAdmin(admin.ModelAdmin):
    list_display = ["teacher", "email"]


# Admin panel for individual lesson applications
@admin.register(IndividualLessonApplication)
class IndividualLessonApplicationAdmin(admin.ModelAdmin):
    list_display = ["user_name", "teacher", "phone", "telegram", "status", ]
    list_editable = ["status", ]
    list_filter = ["status", ]
