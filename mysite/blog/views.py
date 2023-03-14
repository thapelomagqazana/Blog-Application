from django.shortcuts import render
from .models import Post
from django.http import Http404

# Create your views here.

# This view function retrieves all published blog posts and renders them using a template.
def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

# This view function retrieves a single blog post based on its ID and renders it using a template.
def post_detail(request,id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Posts found.")
    
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )