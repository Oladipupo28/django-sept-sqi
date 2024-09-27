from django.urls import path
from . import views

app_name = 'artist'

urlpatterns = [
    path('', views.home, name="home"),
    path("artist_list/", views.artist_list, name="artist_list"),
    path("album_list/", views.album_list, name="album_list"),
    path("artist-detail/<int:artist_id>/", views.artist_detail, name="artist_detail"),
    path("album-detail/<int:album_id>/", views.album_detail, name="album_detail"),
]