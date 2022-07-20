from django.urls import path, include
from books_app.views import *


from books_app.views import (
    create_book,
    show_book,
    show_books,
    edit_book,
)


# URLConf:
urlpatterns = [
    path("create/", create_book,  name="create_book"),
    path("", show_books, name="show_books"),
    path("<int:pk>/", show_book, name="book_detail"),
    # path("new/", create_book, name="book_new"),
    # path("edit/", edit_book, name="book_edit"),
]



