from django.db import models

# Create your models here.

class Book(models.Model):
   title = models.CharField(max_length=125)
   author = models.CharField(max_length=100)
   pages = models.IntegerField()
   isbn = models.IntegerField()
   book_cover_url = models.URLField(null=True, blank=True)
   is_in_print = models.BooleanField()
   pub_date = models.DateField()
   # description = models.TextField()
   # imagef = models.URLField(null=True, blank=True)

   def __str__(self):
       return self.name + ' by ' + self. author
