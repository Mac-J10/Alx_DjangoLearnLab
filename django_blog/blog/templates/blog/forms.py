from django import forms
from django.contrib.auth.models import User
from blog.models import Post
from blog.models import Comment
from .forms import CommentForm
from django.views.generic import DetailView

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']  # you can add 'first_name', 'last_name', etc.

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['comment_form'] = CommentForm()
        return ctx
