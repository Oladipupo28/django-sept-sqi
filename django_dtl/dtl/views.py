from django.shortcuts import render

# Create your views here.
def new_view(request):
    return render(request, 'dtl/dtl_example.html')
