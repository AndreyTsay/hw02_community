from django.shortcuts import render, get_object_or_404
from .models import Post, Group


NUMBER_OF_POSTS: int = 10


def index(request):
    posts = Post.objects.all()[:NUMBER_OF_POSTS]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NUMBER_OF_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
