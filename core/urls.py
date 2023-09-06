from django.urls import path
from .views import home, login, course_details, course_delete, confirm_course_delete, update_course

urlpatterns = [
    path('', home, name='Home'),
    path('courses/<int:id>', course_details, name='Course-Details'),
    path('delete_courses/<int:id>', course_delete, name='Course-Delete'),
    path('update_courses/<int:id>', update_course, name='Course-Update'),
    path('confirm_delete_courses/<int:id>', confirm_course_delete, name='Confirm-Course-Delete'),
    path('login', login, name='Login-Page'),
]