from django.shortcuts import render, get_object_or_404
from .models import Post, Category
import datetime


def index(request):
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lt=datetime.datetime.now()
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post_list = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lt=datetime.datetime.now()
        ), pk=post_id
    )
    return render(request, 'blog/detail.html', {'post': post_list})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(
            slug=category_slug,
            is_published=True,
        )
    )
    post_list = Post.objects.filter(
        pub_date__lt=datetime.datetime.now(),
        is_published=True,
        category=category
    )
    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': post_list})
