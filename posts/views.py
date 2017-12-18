from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.template.context_processors import request

# Create your views here.

def index(request):
  #  return HttpResponse('hello post')
  
    posts = Posts.objects.all()[:10]
    
    context = {
            'title':'latest posts',
            'posts':posts
        }
      
    return render(request, 'posts/index.html',context)

def details(request, id):
    post = Posts.objects.get(id = id)
    context = {
        'post':post
        }
    return render(request, 'posts/details.html',context)