from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages

# Create your views here.
def index(request):
    data= Student.objects.all()
    context={"data":data}
    return render(request, "index.html",context)


def insert(request):
    data= Student.objects.all()
    context={"data":data}
    if request.method == "POST":
        
       name=request.POST.get('name')
       email = request.POST.get('email')
       age=request.POST.get('age')
       gender=request.POST.get('gender')
       print(name,age,email,gender)
       query=Student(name=name,age=age,email=email,gender=gender)
       query.save()
       messages.success(request,"Data Inserted Successfully")
       return redirect("/")
    return render(request, 'index.html')
    
def update(request,id):
    if request.method == "POST":
        
       name=request.POST.get('name')
       email = request.POST.get('email')
       age=request.POST.get('age')
       gender=request.POST.get('gender')
       edit = Student.objects.get(id=id)
       edit.name = name
       edit.email = email
       edit.age = age
       edit.gender = gender
       edit.save()

       messages.info(request,"Data updated Successfully")
       return redirect("/")
    d= Student.objects.get(id=id)
    context={"d":d}
    
    return render(request, "update.html",context)

def delete(request,id):
    
    d= Student.objects.get(id=id)
    d.delete()
    messages.warning(request,"Data Deleted Successfully")
    return redirect("/")
    

def about(request):
    return render(request, "about.html")
