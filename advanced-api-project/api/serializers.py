from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book instances.
    - author: nested representation via AuthorSerializer
    - title: title of the book
    - publication_year: must not be in the future
    """
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year']

    def validate_publication_year(self, value):
        """
        Ensure publication_year is not greater than the current year.
        Raises serializers.ValidationError on failure.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year ({value}) cannot exceed {current_year}."
            )
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author.name and nests a dynamic list of related books.
    The 'books' field uses the related_name on Book.author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']