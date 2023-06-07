from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.filter(is_completed=False)
    # print(tasks)
    context =  {
        'tasks': tasks
    }
    return render(request, 'home.html', context)

def show_completed(request):
    completed = Task.objects.filter(is_completed=True)
    print(completed)
    context = {
        'completed': completed
    }
    return render(request, home.html, context)
