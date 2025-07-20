# CRUD Operations for `Book` Model

## 1. CREATE
```bash
python manage.py shell

book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

# Expected Output: Nineteen Eighty-Four