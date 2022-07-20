from django import forms
from .models import Book, Magazine

# for books:
try:
    from books_app.models import Book

    class BookForm(forms.ModelForm):
        class Meta:
            model = Book
            # exclude = []
            # related to the http://localhost:8000/create/ page
            fields = [
                "title",
                "author",
                "description",
                "image",
            ]

except Exception:
    pass


try:
    from books_app.models import Magazine

    class MagazineForm(forms.ModelForm):
        class Meta:
            model = Magazine
            # exclude = []
            # related to the http://localhost:8000/create/ page
            fields = [
                "title",
                "release_cycle",
                "description",
                "image",
            ]

except Exception:
    pass


