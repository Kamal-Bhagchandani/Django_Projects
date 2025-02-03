from django.shortcuts import redirect, render

from .forms import PostForm
from .models import UserPost

# Create your views here.
def createPost(request):
    form  = PostForm()
    return render(request,"createPost.html", {'form':form})

def uploadPost(request):
    form = PostForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
    else:
        print("Error in Form")
    return redirect('home')

def viewPost(request):
    posts = UserPost.objects.all()
    return render(request,'home.html',{'posts':posts})

def deletePost(request,id):
    post=UserPost.objects.get(id=id)
    post.delete()
    return redirect('viewPost')