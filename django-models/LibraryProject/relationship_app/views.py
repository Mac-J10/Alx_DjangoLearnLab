from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Libraryfrom django.views.generic.detail import DetailView
from .models import Library

def list_books(request):
    books = Book.objects.all()  # ✅ This is the missing line
    return render(request, 'relationship_app/list_books.html', {'books': books})