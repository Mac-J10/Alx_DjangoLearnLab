# CRUD Operations for `Book` Model

## 1. CREATE
```bash
python manage.py shell

book.delete()
print(Book.objects.all())
# Expected Output: <QuerySet []>