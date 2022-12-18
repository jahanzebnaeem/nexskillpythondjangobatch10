from django.shortcuts import render
from django.utils import timezone
from blog.models import Post, Comment
from django.views.generic import (TemplateView,ListView)

# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'

# ================================

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
