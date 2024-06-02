from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, CommentView
from .models import *
from .forms import PostForms

class PostList(ListView):
    model = Post
    ordering = '-dateCreations'
    template_name = 'post.html'
    context_object_name = 'posts'


class PostCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PostForms
    model = Post
    template_name = 'post_create.html'
    context_object_name = 'create'


class Comment(LoginRequiredMixin, CommentView):
    model = Comment
    form_class = PostForms
    ordering = '-dateCreations'
    template_name = 'comment.html'
    context_object_name = 'comment'