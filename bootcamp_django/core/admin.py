from django.contrib import admin
from .models import Course, Musician, Album

# Register your models here.

admin.site.register(Course)
admin.site.register(Musician)
admin.site.register(Album)