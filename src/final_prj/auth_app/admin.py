from django.contrib import admin

from .models import Profile


# Admin panel for user profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "city", "status"]
    list_editable = ["status"]


