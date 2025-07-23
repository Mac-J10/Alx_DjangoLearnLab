# CRUD Operations for `Book` Model

## 1. CREATE
```bash
python manage.py shell

from bookshelf.models import Book

book.delete()
print(Book.objects.all())
# Expected Output: <QuerySet []>