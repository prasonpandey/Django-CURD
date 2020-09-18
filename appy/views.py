from django.shortcuts import render, redirect
from .forms import Registration
from .models import User
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
    
    form = Registration()
    students = User.objects.all()
    return render(request,'appy/add_show.html',{'form':form,'students':students})

def delete(request,pk):
    if request.method == 'POST':
        student = User.objects.get(id=pk)
        student.delete()
        return redirect("/")
    return redirect('/')



def update(request,pk):
    if request.method == 'POST':
        student = User.objects.get(id=pk)
        form = Registration(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:

        student = User.objects.get(id=pk)
        form = Registration(instance=student)

    return render(request,'appy/update.html',{'form':form})