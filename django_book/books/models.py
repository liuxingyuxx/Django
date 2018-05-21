from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    #pub_books = models.ForeignKey('Book', on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(blank=True, max_length=50)
    city = models.CharField(max_length=60, blank=True)
    state_province = models.CharField(max_length=30, verbose_name='省名',blank=True )
    country = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True,null=True)
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    au_books = models.ForeignKey('Book',on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True, null=True)
    def __str__(self):
        return (self.first_name, self.last_name) 

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, null=True)
    publication_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.title

