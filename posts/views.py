from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from cloudinary.forms import cl_init_js_callbacks
#whenever we deal with models we need to import them
from .models import Post
# here we have to import forms
#from .forms import PostForm
# Create your views here.
def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            print("Hello its valid")
            # Redirect to Home
            return HttpResponseRedirect('/')
        else:
            # No,Show Error
            print("its not valid")
            return HttpResponseRedirect(form.errors.as_json())
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request, 'posts.html', {'posts': posts})




def delete(request, post_id):
    #Find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')
# this is for Edit



def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    # Find post
    # if request.method == "GET":
    # post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        # editpost = Post.objects.get(id=post_id)
        form = PostForm(request.POST, request.FILES, instance=post)
        form.save()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("not valid")
    return render(request, 'edit.html', {'post': post})



def LikeView(request, post_id):
    new_value = Post.objects.get(id=post_id)
    new_value.likes += 1
    new_value.save()
    return HttpResponseRedirect('/')