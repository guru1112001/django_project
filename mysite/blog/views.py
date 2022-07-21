from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from .models import post

posts=[
        {
            "author": " manmeet singh ",
            "title": "m hu dank",
            "content":"first post content",
            "date": "19-07-2022",
        },
        {
            "author": " nikku singh burger ",
            "title": "singh buger owner",
            "content":"second  post content",
            "date": "20-07-2022",
        }

]
def home(request):
    context= {
                "posts" : post.objects.all()
        }
    return render(request,"blog/home.html",context)

def about(request):
        return render(request,"blog/about.html",{"tittle":"about"}) 



