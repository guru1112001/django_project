from turtle import title
from django.shortcuts import render
from django.views.generic import ListView
from .models import post


def home(request):
    context= {
                "posts" : post.objects.all()
        }
    return render(request,"blog/home.html",context)

class postlistview(ListView):
    model=post
    template_name =  "blog/home.html"
    context_object_name = "posts"
    ordering= ["-date"]

def about(request):
        return render(request,"blog/about.html",{"tittle":"about"}) 



