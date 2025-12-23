from django.shortcuts import render
from todos.models import task



def home(request):
    tasks=task.objects.filter(is_completed=False)
    context={
        "task":tasks
    }
    
    return render(request,"home.html",context)