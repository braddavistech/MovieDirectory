from django.urls import path
from . import views

app_name = "mymovies"

urlpatterns = [
    path('Movies', views.index, name='index'),
    path('Movies/Search', views.search_movies, name='search_movies'),
    path('Movies/Details/<str:imdbID>', views.details, name='details'),
    path('Movies/GetMovies', views.get_movies, name='get_movies'),
    path('Movies/AddMovies', views.add_movie, name='add_movie'),
    path('Movies/SaveMovies', views.save_movies, name='save_movies'),
]