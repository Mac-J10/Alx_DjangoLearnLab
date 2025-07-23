from .models import Book
from django.shortcuts import render, redirect
from .forms import ExampleForm
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book_view(request):
    return render(request, 'bookshelf/create_book.html')

def search_books(request):
    query = request.GET.get("q", "")
    if query:
        # Avoid raw SQL or string interpolation
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})