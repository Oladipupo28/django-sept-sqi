from django.shortcuts import render
from .models import Artist
from album.models import Album

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


