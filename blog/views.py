from django.shortcuts import render
from blog.models import BlogArticles
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    model = BlogArticles
    template_name = 'blogs/index.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return BlogArticles.objects.order_by('id')

class DetailView(generic.DetailView):
    model = BlogArticles
    template_name = "blogs/detail.html"
    context_object_name = 'blog_object'
