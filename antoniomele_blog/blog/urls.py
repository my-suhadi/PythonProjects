from django.urls import path

from blog import views

# digunakan utk reverse url dlm fungsi get_absolute_url
app_name = 'blog'

urlpatterns = [
    # path('', views.PostListView.as_view(tag_slug=None), name='postListCbvUrl'),
    path('', views.post_list, name='postListUrl'),
    path('tag/<slug:tag_slug>/', views.post_list, name='postByTagUrl'),
    path('<str:year>/<str:month>/<str:day>/<slug:post>/', views.post_detail, name='postDetailUrl'),
    path('<int:post_id>/share/', views.post_share, name='postShareUrl')
]
