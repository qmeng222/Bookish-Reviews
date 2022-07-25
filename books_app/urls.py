from django.urls import path, include
from books_app.views import *


from books_app.views import (
    create_book,
    show_book,
    show_books,
    edit_book,
    list_reviews,
)


# URLConf:
urlpatterns = [
    path("create/", create_book,  name="create_book"),
    path("", show_books, name="show_books"),
    path("<int:pk>/", show_book, name="show_book"),
    path("<int:pk>/edit/", edit_book, name="edit_book"),
    path("<int:pk>/delete/", delete_book, name="delete_book"),
    path('reviews/', list_reviews, name='list_reveiws'),
]

