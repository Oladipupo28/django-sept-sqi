from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
        else: 
            form = MovieForm()
        return render(request, 'movies/movie_form.html', {'form': form})
    
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render('movie_detail', pk=pk)
        else:
            form = MovieForm(instance=movie)
            return render(request, 'movies/movie_form.html', {'form': form})
        
def confirm_delete(request, book_id):
    movie = get_object_or_404(Movie, pk=book_id)
    return render(request, "movies/confirm_delete.html", {'movie': movie})

def movie_delete(request, book_id):
    movie = get_object_or_404(Movie, pk=book_id)   
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:movie_list')    

