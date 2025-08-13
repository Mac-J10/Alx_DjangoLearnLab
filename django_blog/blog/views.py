from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

@login_required
def profile_view(request):
    # 1. Check for POST requests
    if request.method == 'POST':
        # 2. We pass request.POST into the form
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            # 3. .save() commits the changes to the database
            form.save()
            return redirect('blog:profile')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'blog/profile.html', {'form': form})