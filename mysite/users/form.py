
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from. models import profile

class UserRegistorform(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=100)

    class meta:
        model=User
        fields=[ "email","Username","password1","password2","first_name"]
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']

