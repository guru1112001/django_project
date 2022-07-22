from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegistorform
from django.contrib.auth.decorators import login_required
def resgister(request):
    if request.method=="POST":
            form=UserRegistorform(request.POST)
            if form.is_valid():
                form.save()
                username=form.cleaned_data.get("username")
                messages.success(request,f"Your Account has been created! you are now ableto log-in")
                return redirect('login')
    else:
        form=UserRegistorform()
    return render(request,"users/resgister.html",{"form":form})

@login_required
def profile(request):
    return render(request,"users/profile.html")

