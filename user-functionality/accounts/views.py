from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    return render(request, 'registration.html')
def registrate(request):
    user = User()
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.username = request.POST['email']
    user.password = request.POST['password']
    user.save()
    return redirect(index)