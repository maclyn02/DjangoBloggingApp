from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .add_form import PostForm
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


def post_new(request):
    # If request is POST (i.e) form is being submitted
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', primary_key=post.pk)
    # Else request is GET (i.e) when + button is clicked to request form rendering
    else:
        form = PostForm()
        form_for_frontend = {
            'form': form
        }
        return render(request, 'blog/post_edit.html', form_for_frontend)
