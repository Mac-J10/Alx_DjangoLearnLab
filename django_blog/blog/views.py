
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Post, Comment
from .forms import PostForm, CommentForm, ProfileForm, CustomUserCreationForm
from django.db.models import Q
from django.views.generic import ListView
from .models import Post

class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

# --- Post CRUD Views ---

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['comment_form'] = CommentForm()
        return ctx

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        return self.get_object().author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        return self.get_object().author == self.request.user

# --- Comment CRUD Views ---

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=post_pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.post.pk})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.post.pk})

# --- Authentication & Profile Views ---

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('blog:profile')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})

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

class TagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag = self.kwargs['tag_name']
        return Post.objects.filter(tags__name__iexact=tag).distinct()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tag_name'] = self.kwargs['tag_name']
        return ctx