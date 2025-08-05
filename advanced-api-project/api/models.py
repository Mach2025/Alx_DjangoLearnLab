from django.db import models

# This module defines the models for the API project.
# The Author model represents a book author in the system.
# Each author has a name.
class Author(models.Model):
    name = models.CharField(max_length=100) #The author's full name stored here.


    def __str__(self):
        return self.name  # Returns the author's name when printed.

class Book(models.Model):
    title = models.CharField(max_length=200)#This field stores the title of the book.
    publication_year = models.IntegerField() # This field stores the year the book was published.
    # It is an integer field to represent the year.
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)# This establishes a many-to-one relationship with the Author model.
    # Each book is linked to one author, but an author can have multiple books.
    # The related_name 'books' allows access to all books of an author through the Author instance.

    def __str__(self):
        return f" {self.title }  ({ self.publication_year })"
