from django import forms

try:
    from books_app.models import Book

    class BookForm(forms.ModelForm):
        class Meta:
            model = Book
            fields = [
                "title",
                "author",
                "description",
                "image",
            ]

except Exception:
    pass
