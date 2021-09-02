from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# create new form that inherits from UserCreation form
class UserRegisterForm(UserCreationForm):
    # additional field to add in the form
    email = forms.EmailField()
    
    class Meta:
        # specify model which we want form to interact
        model = User
        # these are field that we want to show in order in the form
        fields = ['username', 'email', 'password1', 'password2' ]


class UserUpdateForm(forms.ModelForm):
    model = User
    fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']