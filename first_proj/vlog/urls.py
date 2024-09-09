from django.urls import path
from vlog import views

urlpattern = [
    path('vlog/', views.vlog, name='vlog'),
    # path('content/', views.content, name='content'),
]