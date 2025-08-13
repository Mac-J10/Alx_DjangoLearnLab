# blog/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def register_view(request):
    # Show blank form or process posted data
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # save() persists the new User to the database
            user = form.save()  
            # log the user in immediately after registration
            login(request, user)  
            return redirect('blog:profile')
    else:
        form = CustomUserCreationForm()

    return render(request, 'blog/register.html', {'form': form})


def login_view(request):
    # Present login form or authenticate posted credentials
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # No form.save() here; login() just creates a session
            login(request, user)
            return redirect('blog:profile')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


@login_required
def profile_view(request):
    # Allow user to update their email (or other profile fields)
    if request.method == 'POST':
        new_email = request.POST.get('email')
        if new_email:
            # assign and save the updated field
            request.user.email = new_email  
            request.user.save()  
        return redirect('blog:profile')

    return render(request, 'blog/profile.html', {
        'email': request.user.email
    })