from django.contrib import admin
from .models import title, author, publication_year

class Book (admin.ModelAdmin):

    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')