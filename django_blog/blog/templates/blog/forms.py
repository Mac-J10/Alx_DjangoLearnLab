from django import forms
from django.contrib.auth.models import User
from .models import Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']  # you can add 'first_name', 'last_name', etc.

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']