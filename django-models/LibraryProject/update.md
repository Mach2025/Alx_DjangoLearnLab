
---
 `update.md`
```markdown
# Update Book Title

```python
# Open the Django shell
# python manage.py shell

from bookshelf.models import Book

# Retrieve the book by its current title
book = Book.objects.get(title="1984")

# Change the title
book.title = "Nineteen Eighty-Four"

# Save changes
book.save()

# Confirm update
print(book.title)

# Expected Output:
# Nineteen Eighty-Four

