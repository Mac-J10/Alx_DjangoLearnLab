from django.urls import path
from .views import list_books, LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view: list all books
    path('books/', list_books, name='book-list'),

    # Class-based view: show details (and books) for one library
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]