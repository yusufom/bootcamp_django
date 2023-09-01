from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course
from .forms import CourseForm
# Create your views here.

def home(request):
    queryset = Course.objects.all()
    # create_course = Course.objects.create(name='C++', price='500')
    # create_course.save()
    get_course = Course.objects.filter(price__gte='400')
    course = Course.objects.get(price='50')

    if request.method == "POST":
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            name = request.POST.get('name')
            price = request.POST.get('price')
            create_course = Course.objects.create(name=name, price=price)
            create_course.save()
            return redirect('/')
        
    else:
        course_form = CourseForm()


    context = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'queryset': queryset,
        'course_form': course_form,
        'get_course': get_course,
        'course': course,
    }
    return render(request, 'core/index.html', context)



def login(request):
    context = {
    }
    return render(request, 'core/login.html', context)



