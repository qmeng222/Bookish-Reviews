from django.db import models
from  django.contrib.auth.models import User

# Create your models below:

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
       return self.title +' (' + self.author +')'

class BookReview(models.Model):
    text = models.TextField()
    reviewer = models.ForeignKey(User, related_name='reviews_by_this_user', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.book) + ' reviewed by ' + str(self.reviewer)


class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.name


class Magazine(models.Model):
    title = models.CharField(max_length=200, unique=False)
    release_cycle = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.URLField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, related_name='magazines')
    creator = models.ForeignKey(User, related_name='magazines', on_delete=models.CASCADE)

    def __str__(self):
       return self.title

class Issue(models.Model):
    magazine = models.ForeignKey(Magazine, related_name='magazine_issues', on_delete=models.CASCADE)
    issue_num = models.CharField(max_length=200, unique=True)
    issue_date = models.DateField()
    description = models.TextField(null=True)
    image = models.URLField(null=True, blank=True)
    pages = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.title


class  Author(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # publications = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return self.name
