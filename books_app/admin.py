from django.contrib import admin
from books_app.models import *

# class BookAdmin(admin.ModelAdmin):
#    pass

# class MagazineAdmin(admin.ModelAdmin):
#    pass

# class GenreAdmin(admin.ModelAdmin):
#    pass

# class IssueAdmin(admin.ModelAdmin):
#    pass

# Register your models here.

admin.site.register(Book)
admin.site.register(BookReview)
admin.site.register(Magazine)
admin.site.register(Genre)
admin.site.register(Issue)




