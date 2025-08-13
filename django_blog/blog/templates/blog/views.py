# blog/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def register_view(request):
    # Only on POST do we save a new user
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()            # <-- save() persists the new user
            login(request, user)          # log them in right away
            return redirect('blog:profile')
    else:
        form = CustomUserCreationForm()

    return render(request, 'blog/register.html', {'form': form})


def login_view(request):
    # Only on POST do we authenticate and establish a session
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)         # no save() here—login handles session
            return redirect('blog:profile')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


@login_required
def profile_view(request):
    # Handle GET (view) and POST (update)
    if request.method == 'POST':
        # Grab the new email from the submitted form data
        new_email = request.POST.get('email')
        if new_email:
            request.user.email = new_email
            request.user.save()         # <-- save() commits the change
        return redirect('blog:profile')

    # On GET, just render the profile page with current data
    return render(request, 'blog/profile.html', {
        'email': request.user.email
    })