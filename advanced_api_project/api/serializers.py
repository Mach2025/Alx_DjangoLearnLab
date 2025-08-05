from rest_framework import serializers
from .models import Author
import datetime
from .models import Book

# The BookSerializer handles serialization of Book instances.
# It includes all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']


 # Custom validation to ensure publication_year is not in the future
    def validate(self, data):
        current_year = datetime.date.today().year
        if data['publication_year'] > current_year:
            raise serializers.ValidationError(
                {"publication_year": "Publication year cannot be in the future."}
            )
        return data


class AuthorSerializer(serializers.ModelSerializer):
     # Nested serialization of related books.
    # This uses the related_name 'books' defined in the Book model.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
# This serializer demonstrates how Django REST Framework handles one-to-many relationships.
    # The 'books' field includes all books linked to an author.