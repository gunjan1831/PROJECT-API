from django.contrib import admin
from django.urls import path,include
from movielist_app.views import movie_list



urlpatterns = [
    path('admin/', admin.site.urls),
    path('lists/', movie_list,name='movie_list'),
]