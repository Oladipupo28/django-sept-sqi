from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact(request):
    return HttpResponse("<h1>Contact us at edu.sqi.ng</h1>")

def email(request):
    return HttpResponse("Send us an email at edu.sqi@gmail.com")
