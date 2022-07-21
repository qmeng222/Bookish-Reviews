from django.urls import path, include
from books_app.views import *
# from books_app.views import (
#     create_magazine,
#     show_magazine,
# )


# URLConf:
urlpatterns = [
    path("create/", create_magazine,  name="create_magazine"),
    path("", show_magazines, name="show_magazines"),
    path("<int:pk>/", show_magazine, name="show_magazine"),
    path("edit/", edit_book, name="book_edit"),
    path("<int:pk>/edit/", edit_magazine, name="edit_magazine"),
    path("<int:pk>/delete/", delete_magazine, name="delete_magazine"),
    path("<str:genre_name>/", show_genre_mags, name = "show_genre"),
]



