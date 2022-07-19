from django.contrib import admin
from django.urls import path, include
from books_app.views import show_books


from books_app.views import (
    show_book,
    show_books,
)


# URLConf:
# the include tag allows you include a template inside the current template.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books_app.urls')),
    path('', show_books, name='books_list'),
    # path("<int:pk>/", show_book, name='book_detail'),
]

