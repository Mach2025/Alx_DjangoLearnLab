# Delete the book instance
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Output: Book instance deleted
print(Book.objects.all())  # Should return an empty QuerySet if this was the only book
