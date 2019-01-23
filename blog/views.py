from django.shortcuts import render
from blog.models import BlogArticles
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    model = BlogArticles