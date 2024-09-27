from django.shortcuts import render, get_object_or_404
from .models import Artist
from album.models import Album
from django.http import HttpResponseNotFound
# Create your views here.
def home(request):
    return render(request, 'music/home.html')

def artist_list(request):
    artists = Artist.objects.all().order_by('debut_year')
    return render(request, 'music/artist_list.html', {'artists': artists})

def album_list(request):
    albums = Album.objects.all().order_by('released_date')
    return render(request, 'music/album_list.html', {'albums': albums})     

    # the_albums = Album.objects.all().order_by('released_date')
    # context = {
    #     'all_the_artists': the_artists,
    #     'all_the_albums': the_albums
# }
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    context = {"artist": artist}
    return render(request, 'music/artist_detail.html', context)

def album_detail(request, artist_id):
    album = get_object_or_404(Album, pk=artist_id)
    context = {"album": album}
    return render(request, 'music/album_detail.html', context)
