from django.contrib import admin
from books_app.models import *

class BookAdmin(admin.ModelAdmin):
   pass

class MagazineAdmin(admin.ModelAdmin):
   pass

# Register your models here.

admin.site.register(Book, BookAdmin)

admin.site.register(Magazine, MagazineAdmin)
