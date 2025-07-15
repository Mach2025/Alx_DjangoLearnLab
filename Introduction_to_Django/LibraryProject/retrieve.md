
---

`retrieve.md`
```markdown
# Retrieve Book Instance

```python
# Open the Django shell
# python manage.py shell

from bookshelf.models import Book

# Get all books in the database
books = Book.objects.all()

# Loop and print each book's details
for book in books:
    print(book.title, book.author, book.publication_year)

# Expected Output:
# 1984 George Orwell 1949

