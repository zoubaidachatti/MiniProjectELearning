from django.shortcuts import redirect, render
from .models import Post
from django.contrib import messages
# Create your views here.

#home
def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})
# add
def add(request):
    if request.method=='POST':
        title=request.POST['title']
        detail=request.POST['detail']
        Post.objects.create(title=title,detail=detail)
        messages.success(request,'Data has been added')
    return render(request,'add.html')
# update
def update(request,id):
    if request.method=='POST':
        title=request.POST['title']
        detail=request.POST['detail']
        Post.objects.filter(id=id).update(title=title,detail=detail)
        messages.success(request,'Data has been updated')
    post=Post.objects.get(id=id)
    return render(request,'update.html',{'post':post})
# delete
def delete(request,id):
    Post.objects.filter(id=id).delete()
    return redirect('/admin')
