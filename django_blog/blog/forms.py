from django import forms
from .models import Post
from django.contrib.auth.models import User
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date']
        
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']