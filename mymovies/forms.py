from django import forms
from .models import *

class NewMovieForm(forms.Form):
    name = forms.CharField(label='Insert New Movie Title', max_length=100, required=True)

class SaveNewMovieForm(forms.Form):
    Title = forms.CharField(label='Movie Title', max_length=100)
    Year = forms.CharField(label='Year', max_length=4)
    Rated = forms.CharField(label='Rating', max_length=15)
    Released = forms.CharField(label='Released Date', max_length=20)
    Runtime = forms.CharField(label='Runtime', max_length=20)
    Genre = forms.CharField(label='Genre', max_length=100)
    Director = forms.CharField(label='Director', max_length=200)
    Actors = forms.CharField(label='Actors', max_length=500)
    Plot = forms.CharField(label='Plot', max_length=700)
    Language = forms.CharField(label='Language', max_length=50)
    Country = forms.CharField(label='Country', max_length=50)
    Awards = forms.CharField(label='Awards', max_length=100)
    Poster = forms.CharField(label='Poster', max_length=150)
    rottenRating = forms.CharField(label='Rotten Tomato Rank', max_length=20)
    imdbRating = forms.CharField(label='IMDB Rank', max_length=10)
    criticRating = forms.CharField(label='Metacritic Rank', max_length=10)
    imdbID = forms.CharField(label='IMDB ID', max_length=30)
    Type = forms.CharField(label='Type', max_length=50)
    DVD = forms.CharField(label='DVD', max_length=40)
