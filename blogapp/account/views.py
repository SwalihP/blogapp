from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

def register(request):
    if(request.method=='POST'):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if(p==cp):
            user=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            user.save()
            return user_login(request)
        else:
            messages.error(request,"INCORRECT PASSWORD")

    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('application:appbase')
        else:
            messages.error(request, "INVALID USERNAME OR PASSWORD")

    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return home(request)
