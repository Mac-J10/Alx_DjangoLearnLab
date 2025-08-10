# api/urls.py
from django.urls import include, path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('api/', include('api.urls')),
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Retrieve a single book by its ID
    path('books/', BookDetailView.as_view(), name='book-detail'),

    # Create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update an existing book (PUT/PATCH)
    path('books/update/', BookUpdateView.as_view(), name='book-update'),

    # Delete a book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
]