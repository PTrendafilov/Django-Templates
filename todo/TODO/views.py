from asyncio import tasks
from django.shortcuts import render
from TODO.models import *
from django.http import HttpResponse
# Create your views here.



def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks':tasks})