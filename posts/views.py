from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    queryset = Post.objects.all()
