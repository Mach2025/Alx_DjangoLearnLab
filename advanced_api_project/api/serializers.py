from rest_framework import serializers
from .models import Author
import datetime
from .models import Book

# The BookSerializer handles serialization of Book instances.
# It includes all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'# This will include all fields from the Book model


 # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
     # Nested serialization of related books.
    # This uses the related_name 'books' defined in the Book model.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = [ 'name', 'books']
# This serializer demonstrates how Django REST Framework handles one-to-many relationships.
    # The 'books' field includes all books linked to an author.