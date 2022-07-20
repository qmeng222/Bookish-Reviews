from django.urls import path, include
from books_app.views import *


from books_app.views import (
    create_magazine,
    show_magazine,
    show_magazines,
    edit_magazine,
)


# URLConf:
urlpatterns = [
    path("create/", create_magazine,  name="create_book"),
    path("", show_magazines, name="show_magazines"),
    path("<int:pk>/", show_magazine, name="magazine_detail"),
    # path("edit/", edit_book, name="book_edit"),
]



