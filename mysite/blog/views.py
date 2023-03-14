from django.shortcuts import render, get_list_or_404
from .models import Post
from django.http import Http404

# Create your views here.

# This view function retrieves all published blog posts and renders them using a template.
def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

# This view function retrieves a single blog post based on its ID and renders it using a template.
def post_detail(request,id):
    # The 'get_list_or_404' funct. ensures that only published blog post are displayed,
    # and returns a 404 error if the post is not found or is not published.
    post = get_list_or_404(Post,
                           id=id,
                           status=Post.Status.PUBLISHED)
    
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})