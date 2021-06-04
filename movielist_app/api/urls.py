from django.contrib import admin
from django.urls import path,include
#from movielist_app.api.views import movie_list,movie_details

from movielist_app.api.views import MovieDetailsAV, MovieListAV



urlpatterns = [

    path('lists/', MovieListAV.as_view(),name='movie_list'),
    path('<int:pk>',MovieDetailsAV.as_view(),name='movie_details'),
]