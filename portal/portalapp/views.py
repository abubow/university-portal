from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import MyAuthForm

def login_view(request):
    error_message = ""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid login credentials. Please try again."
    return render(request, 'login/index.html', {'error_message': error_message})


def index(request):
    return render(request, 'base.html')