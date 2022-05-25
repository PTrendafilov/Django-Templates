from asyncio import tasks
from django.shortcuts import redirect, render
from TODO.models import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by('id')
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

def complete_task(request,id):
    task=Task.objects.get(id=id)
    task.is_finished = True
    task.save()
    return redirect(index)

def delete(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect(index)

def edit(request,id):
    task=Task.objects.get(id=id)
    return render(request, 'edit.html', {'task':task})

def edit_task(request,id):
    task=Task.objects.get(id=id)
    task_text = request.POST['task_text']
    task.task_text=task_text
    deadline = request.POST['deadline']
    task.deadline=deadline
    is_finished = request.POST['is_finished']
    task.is_finished=is_finished
    task.save()
    return redirect(index)
