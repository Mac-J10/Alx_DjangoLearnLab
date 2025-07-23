from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Customize the admin interface to include date_of_birth and profile_photo.
    """
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "date_of_birth",
        "is_staff",
    )
    readonly_fields = ("profile_photo",)