from django.contrib.auth.models import User
from django.db import models

from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='static/img')
    def __str__(self):
        return self.name



class Article(models.Model):
    author = models.ForeignKey(Author, related_name='author' , on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    summary = models.TextField()
    firstParagraph  = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title



