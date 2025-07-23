import os
import django

# Set up environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)


# Sample outputs
if __name__ == "__main__":
    print("Books by 'Jane Doe':")
    for book in get_books_by_author("Jane Doe"):
        print(book.title)

    print("\nBooks in 'City Library':")
    for book in get_books_in_library("City Library"):
        print(book.title)

    print("\nLibrarian at 'City Library':")
    print(get_librarian_for_library("City Library").name)
