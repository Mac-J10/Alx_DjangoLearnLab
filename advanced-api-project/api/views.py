# api/views.py
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    Retrieves all Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

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
    permission_class = [IsStaffOrReadOnly]
    permission_classes = [permissions.IsAuthenticated]