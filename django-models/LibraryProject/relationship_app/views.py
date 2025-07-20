from django.shortcuts import render, redirect
from django.http import HttpResponse

# Authentication imports
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Book, Library

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)         # ← UserCreationForm()
        if form.is_valid():
            form.save()
            return redirect('relationship_app:login')
    else:
        form = UserCreationForm()                     # ← UserCreationForm()

    return render(
        request,
        'relationship_app/register.html',            # ← relationship_app/register.html
        {'form': form}
    )

def list_books(request):
    books = Book.objects.all()                      # ← Book.objects.all()
    return render(
        request,
        'relationship_app/list_books.html',           # ← relationship_app/list_books.html
        {'books': books}
    )