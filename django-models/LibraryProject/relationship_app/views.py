from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile


# Authentication imports
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)         # ← UserCreationForm()
        if form.is_valid():
            form.save()
            return redirect('relationship_app:login')
    else:
        form = UserCreationForm()                     # ← UserCreationForm()

    return render(
        request,
        'relationship_app/register.html',            # ← relationship_app/register.html
        {'form': form}
    )

def list_books(request):
    books = Book.objects.all()                      # ← Book.objects.all()
    return render(
        request,
        'relationship_app/list_books.html',           # ← relationship_app/list_books.html
        {'books': books}
    )

class LibraryDetailView(DetailView):
    model = Library                                  # ← Library
    template_name = 'relationship_app/library_detail.html'  # ← relationship_app/library_detail.html

