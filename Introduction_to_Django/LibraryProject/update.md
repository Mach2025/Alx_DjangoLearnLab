# Update the title of the book
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Output: Book title successfully updated
print(book.title)  # Nineteen Eighty-Four
