from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    # path('', views.post_list, name='post_url'),
    path('', views.PostListView.as_view(), name='post_list_cbv'),
    path('<str:year>/<str:month>/<str:day>/<slug:post>/', views.post_detail, name='post_detail_url'),
]
