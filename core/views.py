from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course
from .forms import CourseForm, CourseModelForm
# Create your views here.

def home(request):
    queryset = Course.objects.all()
    # create_course = Course.objects.create(name='C++', price='500')
    # create_course.save()
    get_course = Course.objects.filter(price__gte='400')
    course_model_form = CourseModelForm()

    # if request.method == "POST":
    #     course_form = CourseForm(request.POST)
    #     if course_form.is_valid():
    #         name = request.POST.get('name')
    #         price = request.POST.get('price')
    #         create_course = Course.objects.create(name=name, price=price)
    #         create_course.save()
    #         return redirect('/')
    
    if request.method == "POST":
        course_model_form = CourseModelForm(request.POST)
        if course_model_form.is_valid():
            course_model_form.save()
            return redirect('Home')
        
    else:
        course_model_form = CourseModelForm()


    context = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'queryset': queryset,
        # 'course_form': course_form,
        'course_model_form': course_model_form,
        'get_course': get_course,
    }
    return render(request, 'core/index.html', context)

def course_details(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }
    return render(request, 'core/course_detail.html', context)

def confirm_course_delete(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }
    return render(request, 'core/confirm_delete_course.html', context)

def course_delete(request, id):
    course_to_delete = Course.objects.get(id=id)
    course_to_delete.delete()
    return redirect('Home')

def update_course(request, id):
    course = Course.objects.get(id=id)
    # course_model_form = CourseModelForm(instance=course)
    # if request.method == "POST":
    #     course_model_form = CourseModelForm(request.POST, instance=course)
    #     if course_model_form.is_valid():
    #         course_model_form.save()
    #         return redirect('Home')
    
    if request.method == "POST":
        course_form = CourseForm(request.POST, initial={'name': course.name, 'price': course.price})
        if course_form.is_valid():
            name = request.POST.get('name')
            price = request.POST.get('price')
            course.name = name
            course.price = price
            course.save()
            return redirect('/')
        
    else:
        course_form = CourseForm(initial={'name': course.name, 'price': course.price})
        
    context = {
        'course_model_form': course_form,
        'course': course,
    }
    return render(request, 'core/course_update.html', context)

def login(request):
    context = {
    }
    return render(request, 'core/login.html', context)



