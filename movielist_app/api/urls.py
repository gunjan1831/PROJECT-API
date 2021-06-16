from django.contrib import admin
from django.urls import path,include
#from movielist_app.api.views import movie_list,movie_details

from movielist_app.api.views import WatchDetailsAV, WatchListAV,StreamPlatformAV,StreamPlatformDetailsAV,ReviewList,ReviewDetails,ReviewCreate



urlpatterns = [

    path('lists/', WatchListAV.as_view(),name='movie_list'),
    path('<int:pk>',WatchDetailsAV.as_view(),name='movie_details'),
    path('stream/<int:pk>',StreamPlatformDetailsAV.as_view(),name='stream-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),

     path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
     path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
     path('stream/review/<int:pk>', ReviewDetails.as_view(), name='review-detail'),

    # path('review/', ReviewList.as_view(), name='review'),
    # path('review/<int:pk>', ReviewDetails.as_view(), name='review-detail'),
]