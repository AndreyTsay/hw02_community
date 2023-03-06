from django.shortcuts import render, get_object_or_404
from .models import Post, Group

MAGIC_NUMBER: int = 10


def index(request):
    posts = Post.objects.all()[:MAGIC_NUMBER]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.groups.all()[:MAGIC_NUMBER]
    title = 'Лев Толстой – зеркало русской революции.'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
