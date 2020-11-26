from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post


# Create your views here.

def post_list(request):
    all_post = Post.objects.all()
    cx = {
        'key_posts': all_post
    }

    return render(request, 'blog/post/list.html', cx)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    cx = {
        'key_post': post
    }

    return render(request, 'blog/post/detail.html', cx)


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'post_obj'
    paginate_by = 3
    template_name = 'blog/post/list.html'
