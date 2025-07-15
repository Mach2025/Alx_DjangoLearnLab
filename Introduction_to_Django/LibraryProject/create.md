<!-- # Create a Book instance
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output: Book object created with ID, e.g., <Book: 1984>
print(book) -->

# ✅ Create a Book Instance

```python
# Open the Django shell first
# python manage.py shell

from bookshelf.models import Book

# Create a new book record
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Print the book to confirm creation
print(book)

# Expected Output:
# <Book: 1984>

