# Advanced API Project

This is a Django REST Framework project for managing books and authors.

## Features
- CRUD operations for books using DRF generic views
- Permissions: Only authenticated users can create, update, or delete
- Nested serialization of authors and books

## API Endpoints

| Method | Endpoint         | Description            |
|--------|------------------|------------------------|
| GET    | /books/          | List all books         |
| POST   | /books/          | Create a new book      |
| GET    | /books/<id>/     | Retrieve a single book |
| PUT    | /books/<id>/     | Update a book          |
| DELETE | /books/<id>/     | Delete a book          |

## Permissions
- Anyone can view books
- Only logged-in users can add, edit, or delete books

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
