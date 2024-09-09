from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def vlog(request):
    return HttpResponse("<h1>My first vlogging video</h1>")

# def content(request):
#     return HttpResponse("<h1>I love content creation</h1>")