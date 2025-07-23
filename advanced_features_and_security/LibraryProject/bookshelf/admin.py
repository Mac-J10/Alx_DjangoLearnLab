from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
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

# Register CustomUser using admin.site.register
admin.site.register(CustomUser, CustomUserAdmin)



# Register your models here.
from django.contrib import admin
from .models import Book

#admn inerface customization

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns
    list_filter = ('author', 'publication_year')  # Filter sidebar options
    search_fields = ('title', 'author')  # Enable search bar

admin.site.register(Book, BookAdmin)