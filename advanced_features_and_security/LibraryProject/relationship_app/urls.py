from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView, register
from . import views
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
     path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
        # relationship_app/urls
    path('admin-only/', views.admin_view, name='admin_view'),
    path('librarian-only/', views.librarian_view, name='librarian_view'),
    path('member-only/', views.member_view, name='member_view'),
    
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    
    path("add_book/", views.add_book, name="debug_add_book"),
    path("edit_book/", views.edit_book, name="debug_edit_book"),


    # path('books/add/', views.add_book, name='add_book'),
    # path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    # path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
