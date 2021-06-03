from django.contrib import admin
from django.urls import path,include
from movielist_app.api.views import movie_list,movie_details



urlpatterns = [

    path('lists/', movie_list,name='movie_list'),
    path('<int:pk>',movie_details,name='movie_details'),
]