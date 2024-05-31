from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForms

class PostList(ListView):
    model = Post
    ordering = '-dateCreations'
    template_name = 'Post.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PostForms
    model = Post
    template_name = 'post_create.html'
    context_object_name = 'create'


