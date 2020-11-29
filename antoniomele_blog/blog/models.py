from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    objects = models.Manager()  # default manager
    published = PublishedManager()  # custom manager

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    # jika related_name tidak diisi otomatis bernama post_set
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts_user')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='draft')

    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('blog:postDetailUrl',
                       args=[
                           self.publish.year,
                           self.publish.month,
                           self.publish.day,
                           self.slug
                       ])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    # jika related_name tdk diisi otomatis bernama comment_set
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_post')
    nama = models.CharField(max_length=80)
    email = models.EmailField()
    isi = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "Komentar oleh {} pada {}".format(self.nama, self.post)
