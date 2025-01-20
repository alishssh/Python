from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()

class Books(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')


