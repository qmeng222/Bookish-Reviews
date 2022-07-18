from django.db import models

# Create your models here.

class Book(models.Model):
   title = models.CharField(max_length=200, unique=True)
   author = models.CharField(max_length=200)
   pages = models.SmallIntegerField(null=True)
   isbn = models.BigIntegerField(null=True)
   is_in_print = models.BooleanField(null=True)
   pub_date = models.DateField()
   book_cover_url = models.URLField(null=True, blank=True)
   description = models.TextField(null=True)
   # imagef = models.URLField(null=True, blank=True)

   def __str__(self):
       return self.title + ' by ' + self. author
