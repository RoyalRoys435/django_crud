from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView, ListView, DetailView
from blog.models import Post
from django.urls import reverse_lazy
# Create your views here.
class PostListView(ListView):
         model = Post
   
class PostCreateView(CreateView):
    model = Post

    fields = ['__all__']

    success_url  = reverse_lazy('blog:all')

class PostDetailView(DetailView):
    models = Post

class PostUpdateView(UpdateView):
    model = Post

    fields = ['__all__']

    success_url  = reverse_lazy('blog:all')

class PostDeleteView(DeleteView):
    model = Post

    fields = ['__all__']

    success_url  = reverse_lazy('blog:all')
