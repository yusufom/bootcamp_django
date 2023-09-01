from django import forms


class CourseForm(forms.Form):
    name = forms.CharField()
    price = forms.FloatField()