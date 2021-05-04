from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-created')
    context = {
        'title': 'Home Page',
        'posts': posts,
    }
    return render(request, 'main/index.html', context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'caption']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post