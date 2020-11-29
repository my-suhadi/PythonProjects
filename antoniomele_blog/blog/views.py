from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import EmailPostForm, CommentForm
from .models import Post
from taggit.models import Tag


# Create your views here.

def post_list(request, tag_slug=None):
    post_obj = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_obj = post_obj.filter(tags__in=[tag])

    # nampilin 3 post perhalaman
    paginator = Paginator(post_obj, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    cx = {
        'pageKey': page,
        'postsKey': posts,
        'tagKey': tag,
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

    all_comments = post.comments_post.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # membuat comment object tp tdk nyimpen k database
            new_comment = comment_form.save(commit=False)
            # masukin post k comment baru
            new_comment.post = post
            # nyimpen comment k database
            new_comment.save()
    else:
        comment_form = CommentForm()

    # dapatkan semua id tag pd sebuah post
    post_all_tags_ids = post.tags.values_list('id', flat=True)

    # dapatkan smua post yg memiliki id tag yg sama
    similar_posts = Post.published.filter(tags__in=post_all_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    cx = {
        'postKey': post,
        'allCommentsKey': all_comments,
        'newCommentKey': new_comment,
        'commentFormKey': comment_form,
        'similarPostsKey': similar_posts,
    }

    return render(request, 'blog/post/detail.html', cx)


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            judul = "{} recommends you read {}".format(cd['nama'], post.title)
            pesan = "Read {} at {}\n\n {}\'s comments: {}".format(post.title, post_url, cd['nama'], cd['komentar'])

            send_mail(judul, pesan, 'my.suhadi@yahoo.com', [cd['email_kepada']])
            sent = True

    else:
        form = EmailPostForm()

    cx = {
        'postKey': post,
        'formKey': form,
        'sentKey': sent
    }

    return render(request, 'blog/post/share.html', cx)


# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts_obj'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'
