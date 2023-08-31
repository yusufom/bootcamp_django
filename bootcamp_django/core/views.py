from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
# Create your views here.

def home(request):
    queryset = Course.objects.all()
    context = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'queryset': queryset,
    }
    return render(request, 'core/index.html', context)



def login(request):
    context = {
    }
    return render(request, 'core/login.html', context)



