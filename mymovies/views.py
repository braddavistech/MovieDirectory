from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from .models import *
from .forms import *
import requests

# Create your views here.

def index(request):
    movies = Movie.objects.order_by('-rottenRating')[:10]
    return render(request, 'mymovies/index.html', {'movies': movies})

def search_movies(request):
    movies = Movie.objects.order_by('Title')
    return render(request, 'mymovies/search.html', {'movies': movies})

def add_movie(request):
    newForm = NewMovieForm()
    return render(request, 'mymovies/add.html', {'form': newForm})

def details(request, imdbID):
    movie = Movie.objects.get(imdbID=imdbID)
    return render(request, 'mymovies/details.html', {'movie': movie})

def get_movies(request):
    url = "http://www.omdbapi.com/?apikey=9b9e6930&t="
    title = request.POST['name']
    title = title.replace(" ", "+")
    api_url = url + title
    response = requests.get(api_url)
    data = response.json()
    print(data)
    rating = data['Ratings']
    imdb = rating[0]['Value']
    rotten = rating[1]['Value']
    critic = rating[2]['Value']
    poster = data['Poster']
    # new = Movie(Title=data['Title'], Year=data['Year'], Rated=data['Rated'], Released=data['Released'], Runtime=data['Runtime'], Genre=data['Genre'], Director=data['Director'], Actors=data['Actors'], Plot=data['Plot'], Language=data['Language'], Country=data['Country'], Awards=data['Awards'], Poster=data['Poster'], rottenRating=rotten, imdbRating=imdb, criticRating=critic, imdbID=data['imdbID'], Type=data['Type'], DVD=data['DVD'])
    # new.save()
    newForm = SaveNewMovieForm(initial={'Title': data['Title'], 'Year': data['Year'], 'Rated': data['Rated'], 'Released': data['Released'], 'Runtime': data['Runtime'], 'Genre': data['Genre'], 'Director': data['Director'], 'Actors': data['Actors'], 'Plot': data['Plot'], 'Language': data['Language'], 'Country': data['Country'], 'Awards': data['Awards'], 'Poster': data['Poster'], 'rottenRating': rotten, 'imdbRating': imdb, 'criticRating': critic, 'imdbID': data['imdbID'], 'Type': data['Type'], 'DVD': data['DVD']})
    return render(request, 'mymovies/new_movie.html', {'form': newForm, 'poster': poster})
    # return HttpResponseRedirect(reverse('mymovies:index'))
    # return render(request, 'mymovies/index.html', {'movies': movies})

def save_movies(request):
    new = Movie(Title=request.POST['Title'], Year=request.POST['Year'], Rated=request.POST['Rated'], Released=request.POST['Released'], Runtime=request.POST['Runtime'], Genre=request.POST['Genre'], Director=request.POST['Director'], Actors=request.POST['Actors'], Plot=request.POST['Plot'], Language=request.POST['Language'], Country=request.POST['Country'], Awards=request.POST['Awards'], Poster=request.POST['Poster'], rottenRating=request.POST['rottenRating'], imdbRating=request.POST['imdbRating'], criticRating=request.POST['criticRating'], imdbID=request.POST['imdbID'], Type=request.POST['Type'], DVD=request.POST['DVD'])
    new.save()
    return HttpResponseRedirect(reverse('mymovies:index'))