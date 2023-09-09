from django.shortcuts import render
from application.models import Blog
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from application.forms import Blogform

@login_required
def apphome(request):
    b = Blog.objects.all()
    return render(request,'apphome.html',{'b':b})


@login_required
def create(request):
    if(request.method=="POST"):
        user=request.user
        a=request.POST['a']
        t=request.POST['t']
        c=request.POST['c']
        i=request.FILES['i']
        b=Blog.objects.create(author=a,title=t,content=c,img=i,user=user)
        b.save()
        return apphome(request)
    return render(request,'create.html')

@login_required
def search(request):
    q=" "
    s=None
    if(request.method=="POST"):
        q=request.POST['q']
        if q:
            s=Blog.objects.filter(Q(title__icontains=q) | Q(author__icontains=q))
        return render(request,'search.html',{'q':q,'s':s})

@login_required
def read(request,s):
    b=Blog.objects.get(id=s)
    return render(request,'read.html',{'b':b})

@login_required
def bloglist(request):
    user=request.user
    b=Blog.objects.filter(user=user)
    return render(request,'bloglist.html',{'b':b})
@login_required
def edit(request,p):
    b=Blog.objects.get(id=p)
    form=Blogform(instance=b)
    if(request.method=='POST'):
        form=Blogform(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            return apphome(request)
    return render(request,'edit.html',{'form':form})

def deleteblog(request,p):
    b=Blog.objects.get(id=p)
    b.delete()
    return bloglist(request)

