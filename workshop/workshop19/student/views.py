from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def index(request):
    students = Student.objects.all()
    return render(request, "student/index.html",{"students":students})
    
def new(request):
    return render(request,"student/new.html")
    
def create(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    birthday = request.POST.get("birthday")
    age = request.POST.get("age")
    
    Student.objects.create(name=name, email=email, birthday=birthday, age=age)
    return redirect("/student")
    