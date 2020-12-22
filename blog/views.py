from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    posts_for_frontend = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', posts_for_frontend)


def post_details(request, primary_key):
    post = get_object_or_404(Post, pk=primary_key)
    post_for_front_end = {
        'post_details': post
    }
    return render(request, 'blog/post_details.html', post_for_front_end)
