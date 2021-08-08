from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# create new form that inherits from UserCreation form
class UserRegisterForm(UserCreationForm):
    # additional field to add in the form
    email = forms.EmailField()
    
    # this class gives nested namespace for configurations and keeps configuration in one place
    # and within the configuration we are saying that model that will be affected is user model
    class Meta:
        # specify model which we want form to interact
        model = User
        # these are field that we want to show in order in form
        fields = ['username', 'email', 'password1', 'password2' ]

