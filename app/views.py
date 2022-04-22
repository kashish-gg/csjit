from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(
        request,'home.html'
    )
def instructions(request):
    return render(
        request,'author_instructions.html'
    )
def topics(request):
    return render(
        request,'topics.html'
    )
def loginPage(request):
    return render(request,'login.html')
def register(request):
    form=UserCreationForm()
    return render(request,'register.html',{'form':form})

def submitPaper(request):
    return render(request,'submit.html')

    # handle functions
def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('app:home')
        else:
            messages.success(request,'Invalid username or password')
            return redirect('app:login')
    else:
        return render(request,'')

def handleRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('app:home')
        else:
            messages.success(request,'Invalid username or password')
            return redirect('app:login')
    else:
        return redirect('app:login')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect('app:home')




    