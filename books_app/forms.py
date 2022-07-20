from django import forms
from .models import Book

try:
    from books_app.models import Book

    class BookForm(forms.ModelForm):
        class Meta:
            model = Book
            # exclude = []
            fields = [
                "title",
                "author",
                "description",
                "image",
            ]

except Exception:
    pass
