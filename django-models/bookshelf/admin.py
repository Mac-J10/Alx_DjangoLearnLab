from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

#admn inerface customization

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns
    list_filter = ('author', 'publication_year')  # Filter sidebar options
    search_fields = ('title', 'author')  # Enable search bar

admin.site.register(Book, BookAdmin)