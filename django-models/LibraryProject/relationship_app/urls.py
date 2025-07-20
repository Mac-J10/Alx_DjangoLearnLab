from django.urls import path
from .views importlist_book LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view: list all books
    path('books/', list_books, name='book-list'),

    # Class-based view: show a specific library’s details
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]


