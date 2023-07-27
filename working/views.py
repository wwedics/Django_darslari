from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

# Django darsliklari 4-qism
class PostPageView(ListView):
    model = Post
    template_name = 'pages/post.html'