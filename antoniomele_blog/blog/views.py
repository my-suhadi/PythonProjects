from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import EmailPostForm, CommentForm
from .models import Post, Comment


# Create your views here.

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

    cx = {
        'postKey': post,
        'allCommentsKey': all_comments,
        'newCommentKey': new_comment,
        'commentFormKey': comment_form
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


class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts_obj'
    paginate_by = 3
    template_name = 'blog/post/list.html'
