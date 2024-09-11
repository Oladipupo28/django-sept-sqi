from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def services(request):
    services_list = ['Data Science', 'Web Development', 'Digital Marketing', 'Cybersecurity', 'Graphic Design', 'Content Creation']
    return render(request, 'portfolio/services.html', {'services': services_list})

def testimonials(request):
    testimonials_dict = {
        'Miss Saida': 'Great service, highly recommend!',
        'Mr Taiwo': 'Professional and timely delivery.',
        'Mrs Chioma': 'Excellent experience, will hire again!'
    } 
    return render(request, 'portfolio/testimonials.html', {'testimonials': testimonials_dict})

def pricing(request):
    pricing_dict ={
        'Data Science': '$1000',
        'Web Development': '$1000',
        'Digital Marketing': '$500',
        'Cybersecurity': '$1100',
        'Graphic Design': '$600',
        'Content Creation': '$400'
    }   
    return render(request, 'portfolio/pricing.html', {'pricing': pricing_dict})

def case_studies(request):
    return render(request, 'portfolio/case_studies.html')

def blog(request):
    return render(request, 'portfolio/blog.html')


