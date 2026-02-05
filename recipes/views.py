from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Iohan',
    })

def contact(request):
    return render(request, 'temp/temp.html')

def about(request):
    return HttpResponse("about")