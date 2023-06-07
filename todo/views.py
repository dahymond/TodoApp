from django.shortcuts import render
from todo.models import Task
from django.http import HttpResponse

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return HttpResponse('The form is submitted')