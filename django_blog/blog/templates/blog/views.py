from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()               # <-- save() commits changes
            return redirect('blog:profile')
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'blog/profile.html', {'form': form})