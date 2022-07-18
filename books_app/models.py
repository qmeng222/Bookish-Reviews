from django.db import models

# Create your models here.

class Book(models.Model):
   title = models.CharField(max_length=200, unique=True)
   author = models.CharField(max_length=200)
   pages = models.SmallIntegerField(null=True)
   isbn = models.BigIntegerField(null=True)
   is_in_print = models.BooleanField(null=True)
   pub_date = models.DateField()
   description = models.TextField(null=True)

   def __str__(self):
       return self.title + ' by ' + self. author
