from django.db import models

# Create your models here.

class Author(models.Model):
    pass

class Book(models.Model):
   title = models.CharField(max_length=200, unique=True)
   author = models.CharField(max_length=200)
   pages = models.SmallIntegerField(null=True)
   isbn = models.BigIntegerField(null=True)
   is_in_print = models.BooleanField(null=True)
   pub_date = models.DateField()
   image = models.URLField(null=True, blank=True)
   description = models.TextField(null=True)

   def __str__(self):
       return self.title + ' by ' + self. author

class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # magazines = models.ManyToManyField("Magazine", related_name='genres')

    def __str__(self):
       return self.name


class Magazine(models.Model):
    title = models.CharField(max_length=200, unique=False)
    release_cycle = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.URLField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, related_name='magazines')

    def __str__(self):
       return self.title


class Issue(models.Model):
    magazine = models.ForeignKey(Magazine, related_name='magazine_issues', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    issue_date = models.DateField()
    description = models.TextField(null=True)
    image = models.URLField(null=True, blank=True)
    pages = models.SmallIntegerField(null=True)


# class BookReview(models.Model):
#     book = models.ForeignKey(Book, related_name='book_reviews', on_delete=models.CASCADE)
#     text = models.TextField()

# class  Author(models.Model):
#     name = models.CharField(max_length=200, unique=True)

