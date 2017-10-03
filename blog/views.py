from django.shortcuts import render
from django.template.response import TemplateResponse
from blog.models import Post


def index(request):
    return render(request, 'blog/index.html', {})

def blog_page(request):
    posts = Post.objects.all()
    return TemplateResponse(request, 'blog/blog.html',  {"posts": posts})
