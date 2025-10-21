from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    author = models.ManyToManyField('Author', related_name='games')
    publisher = models.ForeignKey('Publisher', on_delete=models.PROTECT, related_name='games')

    owner = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='games')

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()

    owner = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='authors')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    owner = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='publishers')

    def __str__(self):
        return self.name