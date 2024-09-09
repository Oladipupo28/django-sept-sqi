from django.urls import path
from blog import views

urlpattern = [
    path('contact-us/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('content/', views.content, name='content'),
]