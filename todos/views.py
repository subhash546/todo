from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from  .models import task


# Create your views here.

def add(request):
    task1=request.POST['task']
    print(task1)
    task.objects.create(task=task1)
    return redirect("home")


def completedTask(request,pk):
    task1 = get_object_or_404(task, pk=pk)
    task1.is_completed=True
    task1.save()
    print(task1)
    
    return redirect("home")


def uncompletedTask(request,pk):
    uncompletask=get_object_or_404(task,pk=pk)
    uncompletask.is_completed=False
    uncompletask.save()
    return redirect('home')


def deletetask(request,pk):
    task1=get_object_or_404(task,pk=pk)
    task1.delete()
    return redirect("home")


def edit(request,pk):
    task1=get_object_or_404(task,pk=pk)
    if request.method=="POST":
       task2=request.POST["task"]
       task1.task=task2
       task1.save()
       
      
       return redirect("home")
        
        
    else:
       
      context={
        "task":task1
       }
        
      return render(request,"edit.html",context)
