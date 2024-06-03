from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import *
from .forms import PostForms, CommentForms

class PostList(ListView):
    model = Post
    ordering = '-dateCreations'
    template_name = 'post.html'
    context_object_name = 'posts'


class PostDetail(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PostForms
    model = Post
    template_name = 'post_create.html'
    context_object_name = 'create'


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForms
    model = Post
    template_name = 'post_edit.html'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class Comment(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = CommentForms
    model = Comment
    ordering = '-dateCreations'
    template_name = 'comment.html'
    context_object_name = 'comment'


class CommentDetail(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Comment
    template_name = 'comment_detail.html'
    context_object_name = 'comments'


