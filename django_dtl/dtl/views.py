from django.shortcuts import render

# Create your views here.
def new_view(request):
    context = {
        'my_name': 'Ogunwo gbemisola',
        'is_dark': 'False',
        'students': ["Abdur_rahman", "Dr. Gafar", "Joseph", "Sam", "Gbemisola", "Emmanuel", "Solomon", "Dr. Shina"]
    }
    return render(request, 'dtl/dtl_example.html', context)
