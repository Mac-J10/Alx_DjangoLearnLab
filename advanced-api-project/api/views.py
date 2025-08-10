# api/views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class BookListView(generics.ListAPIView):
    """
    Lists all Book instances with filtering, searching, and ordering.
    
    filter_backends:
      - DjangoFilterBackend: filter by title, author__name, publication_year
      - SearchFilter: perform text search on title and author__name
      - OrderingFilter: sort results by title or publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

class BookListView(generics.ListAPIView):
    """
    Retrieves all Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields    = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single Book by its primary key.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    Adds custom behavior on creation.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Example: set the creator field if your model has one
        serializer.save(creator=self.request.user)

class BookUpdateView(generics.UpdateAPIView):
    """
    Adds custom behavior on update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Example: log update time or enforce extra validation
        serializer.save(last_modified_by=self.request.user)

class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a Book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]