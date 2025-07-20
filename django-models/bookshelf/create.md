# CRUD Operations for `Book` Model

## 1. CREATE
```bash
python manage.py shell

from bookshelf.models import Book
book = Book.objects.create(
    title="1984", author="George Orwell", publication_year=1949
)
print("Created:", book)

# Expected Output: Book instance successfully created
