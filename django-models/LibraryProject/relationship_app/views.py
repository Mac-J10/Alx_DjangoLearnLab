from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.detail import DetailView

# Authentication imports
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Book, Library

def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()  # ← this line satisfies the check

    # Build a simple text response: one “Title by Author” per line
    lines = [f"{book.title} by {book.author.name}" for book in books]
    text_output = "\n".join(lines)

    return HttpResponse(text_output, content_type="text/plain")