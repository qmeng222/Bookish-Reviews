from django.shortcuts import get_object_or_404, redirect, render

try:
   from books_app.forms import *
   from books_app.models import *
except Exception:
   BookForm = None
   Book = None

# Create your views here.
# CRUD (create, read, update, delete)
# any dynamic data goes into context

def create_book(request):
   context = {}

   form = BookForm(request.POST or None)
   if form.is_valid():
      form.save()
      return redirect("show_books")
   elif BookForm:
        form = BookForm()
   else:
        form = None

   context["form"] = form
   return render(request, "books/create.html", context)


def show_book(request, pk):
    context = {
        'book': Book.objects.get(pk=pk) if Book else None,
    }
    return render(request, "books/detail.html", context)


def show_books(request):
   books =  Book.objects.all()
   context = {
        'books': books if Book else None,
   }
   return render(request, "books/list.html", context)


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {}
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form

    return render(request, 'books/edit.html', context)


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {}
    if request.method == "POST":
        book.delete()
        return redirect("show_books")
    return render(request, "books/delete.html", context)


# for magazine:
def create_magazine(request):
   context = {}

   form = MagazineForm(request.POST or None)
   if form.is_valid():
      form.save()
      return redirect("show_magazines")
   elif MagazineForm:
        form = MagazineForm()
   else:
        form = None

   context["form"] = form
   return render(request, "magazines/create.html", context)


def show_magazine(request, pk):
    context = {
        'magazine': Magazine.objects.get(pk=pk) if Magazine
        else None,
    }
    return render(request, "magazines/detail.html", context)


def show_magazines(request):
    magazines =  Magazine.objects.all()
    context = {
        'magazines': magazines if Magazine else None,
    }
    return render(request, "magazines/list.html", context)

def edit_magazine(request, pk):
    context = {}
    form = MagazineForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form

    return render(request, 'magazines/edit.html', context)


def delete_magazine(request, pk):
    magazine = get_object_or_404(Magazine, pk=pk)
    context = {}
    if request.method == "POST":
        magazine.delete()
        return redirect("show_magazines")
    return render(request, "magazines/delete.html", context)


def show_mag_genres(request, mag_name):
    genre = Genre.objects.get(name=mag_name)
    context = {
        "genre": genre
    }
    return render(request, "magazines/genre_detail.html", context)


def show_genre_mags(request, genre_name):
    g = Genre.objects.get(name=genre_name)
    magazines = Magazine.objects.filter(genre=g)
    context = {
        "magazines": magazines
    }
    return render(request, "magazines/detail.html", context)