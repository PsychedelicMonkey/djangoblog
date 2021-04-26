from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-created')
    context = {
        'title': 'Home Page',
        'posts': posts,
    }
    return render(request, 'main/index.html', context)
