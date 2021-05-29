
from django.shortcuts import render
from movielist_app.models import Movie
from django.http import JsonResponse


def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)

hyyyyy.
