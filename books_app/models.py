from django.db import models

# Create your models here.

class Author(models.Model):
    pass

class Book(models.Model):
   title = models.CharField(max_length=200, unique=True)
   author = models.CharField(max_length=200)
#    author = models.ForeignKey(Author)
   pages = models.SmallIntegerField(null=True)
   isbn = models.BigIntegerField(null=True)
   is_in_print = models.BooleanField(null=True)
   pub_date = models.DateField()
   image = models.URLField(null=True, blank=True)
   description = models.TextField(null=True)

   def __str__(self):
       return self.title + ' by ' + self. author

class Magazine(models.Model):
    title = models.CharField(max_length=200, unique=True)
    release_cycle = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
       return self.title