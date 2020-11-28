from django.urls import path

from blog import views

# digunakan utk reverse url dlm fungsi get_absolute_url
app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='postListCbvUrl'),
    path('<str:year>/<str:month>/<str:day>/<slug:post>/', views.post_detail, name='postDetailUrl'),
    path('<int:post_id>/share/', views.post_share, name='postShareUrl')
]
