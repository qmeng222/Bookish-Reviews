from django.shortcuts import redirect, render

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
    if Book and BookForm:
        inst = Book.objects.get(pk=pk)
        if request.method == "POST":
            form = BookForm(request.POST, instance=inst)
            if form.is_valid():
                form.save()
                return redirect("book_detail", pk=pk)
        else:
            form = BookForm(instance=inst)
    else:
        form = None
    context = {
        "form": form,
    }
    return render(request, "books/edit.html", context)



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
    if Magazine and MagazineForm:
        inst = Magazine.objects.get(pk=pk)
        if request.method == "POST":
            form = MagazineForm(request.POST, instance=inst)
            if form.is_valid():
                form.save()
                return redirect("magazine_detail", pk=pk)
        else:
            form = MagazineForm(instance=inst)
    else:
        form = None
        context = {
        "form": form,
    }
    return render(request, "magazines/edit.html", context)


def update_magazine(request, pk):
    pass