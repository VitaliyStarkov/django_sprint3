from django.utils import timezone
from django.shortcuts import get_object_or_404, render

from blog.constants import MAX_AMOUNT_POSTS
from .models import Post, Category


def filter_and_order_posts(post_manager):
    return post_manager.filter(
                               is_published=True,
                               category__is_published=True,
                               pub_date__lt=timezone.now()
                               ).select_related('author', 'location',
                                                'category')


def index(request):
    posts = filter_and_order_posts(Post.objects)
    return render(
                  request,
                  'blog/index.html',
                  {'post_list': posts[:MAX_AMOUNT_POSTS]}
                 )


def post_detail(request, post_id):
    post = get_object_or_404(
                             filter_and_order_posts(Post.objects),
                             pk=post_id
                             )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
                                 Category,
                                 slug=category_slug,
                                 is_published=True
                                )
    post_list = filter_and_order_posts(category.posts)
    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': post_list}
    )
