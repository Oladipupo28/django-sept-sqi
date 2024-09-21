from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("artist_list/", views.artist_list, name="artist_list"),
    path("album_list/", views.album_list, name="album_list"),
]