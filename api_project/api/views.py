from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import BookViewSet


class BookList(generics.ListAPIView):
    queryset = Book.object.all()
    serializer_class = BookSerializer
    
class BookViewSet (viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookViewSet
    permission_classes = [IsAuthenticated]