from django.shortcuts import render
from blog.models import Post
from haystack.query import SearchQuerySet


def home(request):
    return render(request, 'home.html')


def post_list(request):
    query = request.GET.get('q', '')
    if query:
        # posts = SearchQuerySet().filter(content=query)
        # search with Elasticsearch
        posts = SearchQuerySet().models(Post).filter(content=query)
    else:
        posts = Post.objects.all()

    return render(request, 'posts.html', {'posts': posts})
