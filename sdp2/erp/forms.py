from django import forms
from django.forms import TextInput

from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['regid','name','dept',]
        labels = {'regid':'Registered ID','name':'Your Name','dept':'Department'}