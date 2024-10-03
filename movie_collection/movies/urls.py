from django.urls import path
from . import views

app_name = 'movies'

urlpattern = [
    path('', views.movie_list, name='movie_list'), 
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/create/', views.movie_create, name='movie_create'),
    path('movie/<int:pk>/edit/', views.movie_edit, name='movie_edit'),
    path('movie/<int:book_id>/confirm-delete/', views.confirm_delete, name='confirm_delete'),
    path('movie/<int:book_id>/delete/', views.movie_delete, name='movie_delete'),
]