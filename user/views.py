from django.shortcuts import render, redirect
# this import already made form
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm


def register(request):
    # return render(request, 'blog/about.html')

    if request.method == 'POST':
        # instance of form to use forms which we import
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            # save the input data of form in backend
            form.save()
            # validated form data will be in cleaned_data dictionary
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    # access the form within the template from a variable form using dictionary
    return render(request, 'user/register.html', {'form': form})



@login_required
def profile(request):
    return render(request, 'user/profile.html')
