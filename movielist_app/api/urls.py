from django.contrib import admin
from django.urls import path,include
#from movielist_app.api.views import movie_list,movie_details

from movielist_app.api.views import WatchDetailsAV, WatchListAV,StreamPlatformAV



urlpatterns = [

    path('lists/', WatchListAV.as_view(),name='movie_list'),
    path('<int:pk>',WatchDetailsAV.as_view(),name='movie_details'),

    path('stream/', StreamPlatformAV.as_view(), name='stream')
]