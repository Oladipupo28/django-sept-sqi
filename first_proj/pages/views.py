from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return HttpResponse("<h1>About sqi.edu.ng</h1>")