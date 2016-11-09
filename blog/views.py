from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blog.models import Post


def index(request):
    return render(request, 'blog/index.html')


def login(request):
    pass
    return render(request, 'blog/login.html')


class PostList(ListView):
    template_name = 'blog/post_main.html'
    model = Post

    def get_queryset(self):
        post_list = Post.objects.order_by('-created')
        return post_list
