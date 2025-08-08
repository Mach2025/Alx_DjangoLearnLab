
from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
# List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends =[DjangoFilterBackend, filter.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['title', 'author', 'publication_year']
    
    # Searching (case-insensitive partial match by default)
    search_fields = ['title', 'author']
    
    # Ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

# Retrieve details of a single book by its ID. Accessible to all
class BookDetailView(generics.RetrieveAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer
     permission_classes = [permissions.AllowAny]

# Create a new book. Only authen  ticated users can access.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

  # Save book instance after validation
    def perform_create(self, serializer):
        serializer.save() 
# Update a book by ID. Only authenticated users.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

 # Save updated book instance
    def perform_update(self, serializer):
        serializer.save()
# Delete a book by ID. Only authenticated users.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]



