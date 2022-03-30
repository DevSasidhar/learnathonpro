from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def home(request):
    return render(request, 'erp/home.html', {'title':'KL-Home'})

def about(request):
    return render(request, 'erp/about.html', {'title':'About KLU'})

def new_student(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewS')
    else:
        form=StudentForm()
    return render(request, 'erp/new_student.html', {'title':'Register','form':form})

def view_student(request):
    return render(request, 'erp/view_student.html', {'title':'View Students','students':Student.objects.all()})