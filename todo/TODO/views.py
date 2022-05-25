from asyncio import tasks
from django.shortcuts import redirect, render
from TODO.models import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks':tasks})

def create(request):
    return render(request, 'create.html')

def create_task(request):
    task = Task()
    task_text = request.POST['task_text']
    task.task_text=task_text
    deadline = request.POST['deadline']
    task.deadline=deadline
    task.save()
    return redirect(index)