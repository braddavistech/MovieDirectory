from django import forms
from .models import *

class NewMovieForm(forms.Form):
    name = forms.CharField(label='Insert New Movie Title', max_length=100, required=True)

class SaveNewMovieForm(forms.Form):
    Title = forms.CharField(label='Movie Title', max_length=100)
    Year = forms.CharField(widget = forms.HiddenInput(), label='Year', max_length=4)
    Rated = forms.CharField(widget = forms.HiddenInput(), label='Rating', max_length=15)
    Released = forms.CharField(widget = forms.HiddenInput(), label='Released Date', max_length=20)
    Runtime = forms.CharField(widget = forms.HiddenInput(), label='Runtime', max_length=20)
    Genre = forms.CharField(widget = forms.HiddenInput(), label='Genre', max_length=100)
    Director = forms.CharField(widget = forms.HiddenInput(), label='Director', max_length=200)
    Actors = forms.CharField(widget = forms.HiddenInput(), label='Actors', max_length=500)
    Plot = forms.CharField(label='Plot', max_length=700)
    Language = forms.CharField(widget = forms.HiddenInput(), label='Language', max_length=50)
    Country = forms.CharField(widget = forms.HiddenInput(), label='Country', max_length=50)
    Awards = forms.CharField(widget = forms.HiddenInput(), label='Awards', max_length=100)
    Poster = forms.CharField(widget = forms.HiddenInput(), label='Poster', max_length=150)
    rottenRating = forms.CharField(widget = forms.HiddenInput(), label='Rotten Tomato Rank', max_length=20)
    imdbRating = forms.CharField(widget = forms.HiddenInput(), label='IMDB Rank', max_length=10)
    criticRating = forms.CharField(widget = forms.HiddenInput(), label='Metacritic Rank', max_length=10)
    imdbID = forms.CharField(widget = forms.HiddenInput(), label='IMDB ID', max_length=30)
    Type = forms.CharField(widget = forms.HiddenInput(), label='Type', max_length=50)
    DVD = forms.CharField(widget = forms.HiddenInput(), label='DVD', max_length=40)
