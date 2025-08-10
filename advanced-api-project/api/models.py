from django.db import models

class Author(models.Model):
    """
    Represents an author.
    The 'name' field stores the full name of the author.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book linked to an author.
    - title: the book’s title.
    - publication_year: year the book was published.
    - author: foreign key to Author (one-to-many).
    """
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title} ({self.publication_year})'