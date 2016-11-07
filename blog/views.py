from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def login(request):
    pass
    return render(request, 'blog/login.html')
