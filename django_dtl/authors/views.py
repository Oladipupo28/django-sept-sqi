from django.shortcuts import render
from .models import Author
from library.models import Book
from datetime import datetime

def all_authors(request):
    return render(request, 'authors/all_authors.html')

def book_signings(request):
    return render(request, 'authors/book_signings.html')

def authors_books(request):
    all_authors = Author.objects.all()
    all_books = Book.objects.all()
    year_2000 = datetime(2000, 1, 1)
    old_authors = all_authors.filter(birth_date__lt=year_2000)
    gbemi = Author.objects.get(first_name='Gbemisola', last_name='Oladipupo' )
    django_book = Book.objects.get(title="My first django experience", author=gbemi)
    recently_published = Book.objects.order_by("-published_on")
    sorted_authors = Author.objects.order_by('first_name')
    authors_with_books = Author.objects.exclude(book__isnull=True)

    context = {
        'all_the_authors': all_authors,
        'all_the_books': all_books,
        'old_authors': old_authors,
        'django_book': django_book,
        'recently_published': recently_published,
        'sorted_authors': sorted_authors,
        'authors_with_books': authors_with_books
        
}
    return render(request, 'authors/authors_books.html', context)