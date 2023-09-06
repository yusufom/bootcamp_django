from django import forms
from .models import Course


class CourseForm(forms.Form):
    name = forms.CharField()
    price = forms.FloatField()
    # classes = forms.FloatField()
    
    
class CourseModelForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = '__all__'
        # exclude = ['name']