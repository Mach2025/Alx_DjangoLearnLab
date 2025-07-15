# Retrieve and display all Book instances
from bookshelf.models import Book
books = Book.objects.all()

# Output: QuerySet showing all books
for book in books:
    print(book.title, book.author, book.publication_year)
