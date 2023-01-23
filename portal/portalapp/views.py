from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import MyAuthForm

def login_view(request):
    error_message = ""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            print("user is not none")
            error_message = ""
            login(request, user)
            return redirect('index')
        else:
            # authenticate based on username and password
            user = authenticate(request, username=email, password=password)
            if user is not None:
                print("user is not none")
                error_message = ""
                login(request, user)
                return redirect('index')
            else:
                error_message = "Invalid login credentials. Please try again."
                return render(request, 'login/index.html', {'error_message': error_message})
    return render(request, 'login/index.html', {'error_message': ""})

@login_required(login_url='/login/')
def index(request):
    return render(request, 'main.html')

@login_required(login_url='/login/')
def quizes(request):
    return render(request, 'quizes/index.html')

@login_required(login_url='/login/')
def material(request):
    return render(request, 'material/index.html')

@login_required(login_url='/login/')
def submissions(request):
    return render(request, 'submissions/index.html')

@login_required(login_url='/login/')
def timetable(request):
    return render(request, 'timetable/index.html')

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile/index.html')