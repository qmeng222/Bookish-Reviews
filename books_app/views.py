from django.shortcuts import redirect, render

try:
   from books_app.forms import BookForm
   from books_app.models import Book
except Exception:
   BookForm = None
   Book = None

# Create your views here.

# any dynamic data goes into context:
def show_books(request):
   books =  Book.objects.all()
   context = {
        'books': books if Book else None,
   }
   return render(request, "books/list.html", context)


def show_book(request, pk):
    context = {
        'book': Book.objects.get(pk=pk) if Book else None,
    }
    return render(request, "books/detail.html", context)