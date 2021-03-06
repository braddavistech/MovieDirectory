from django.db import models
from django.core.validators import MinValueValidator
import datetime

class Movie(models.Model):
    Title = models.TextField(max_length=100)
    Year = models.CharField(max_length=4)
    Rated = models.CharField(max_length=15)
    Released = models.TextField(max_length=20)
    Runtime = models.TextField(max_length=20)
    Genre = models.TextField(max_length=100)
    Director = models.TextField(max_length=200)
    Actors = models.TextField(max_length=500)
    Plot = models.TextField(max_length=700)
    Language = models.TextField(max_length=50)
    Country = models.TextField(max_length=50)
    Awards = models.TextField(max_length=100)
    Poster = models.TextField(max_length=150)
    rottenRating = models.TextField(max_length=20)
    imdbRating = models.TextField(max_length=10)
    criticRating = models.TextField(max_length=10)
    imdbID = models.CharField(max_length=30)
    Type = models.TextField(max_length=50)
    DVD = models.TextField(max_length=40)
    def __str__(self):
        return self






