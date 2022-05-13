from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from.import models
from .models import post,date,topic


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
    alltopics = topic.objects.all()
    return render(
        request,'topics.html',{'topics':alltopics}
    )
def dates(request):
    alldates = date.objects.all()
    return render(
        request,'dates.html',{'dates':alldates}
    )
def contact(request):
    return render(
        request,'contact.html'
    )
def postsPage(request):
    allposts = post.objects.all()[::-1]
    return render(
        request,'posts.html',{'posts':allposts}
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
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,'register success')
            return redirect('app:home')
        return redirect('app:register')
    else:
        form=UserCreationForm()
        return redirect('app:register')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect('app:home')

def handlePost(request):
    if request.method =='POST':
        topic = request.POST['topic']
        title = request.POST['title']
        gender = request.POST['gender']
        category = request.POST['category']
        phonenumber = request.POST['phone']
        emailid = request.POST['emailid']
        amountpaid = request.POST['amount_paid']
        accountnumber = request.POST['accountno']
        description = request.POST['description']
        newform=models.post.objects.create()
        newform.user_id=str(request.user.username)
        newform.topic=topic
        newform.gender=gender
        newform.title=title
        newform.category=category
        newform.phonenumber=phonenumber
        newform.emailid=emailid
        newform.amount_paid=amountpaid
        newform.accountno=accountnumber
        newform.description=description
        newform.save()
        messages.success(request, "You Have Successfully Posted")
        return redirect('app:home')
    else:
        messages.error(request, "Signin First!")
        return redirect('app:home')
        
