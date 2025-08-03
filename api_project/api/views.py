from rest_framework.generics import ListAPIView
from django.urls import path
from .models import Book
from .serializers import BookSerializer

class BookList(generic.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer