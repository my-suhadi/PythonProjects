from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='url_home'),
    path('products/', views.products, name='url_product'),
    path('customer/<str:customer_id>/', views.customer, name='url_customer'),
    path('create_order/<str:customer_id>/', views.create_order, name='url_create_order'),
    path('update_order/<str:order_id>/', views.update_order, name='url_update_order'),
    path('delete_order/<str:order_id>/', views.delete_order, name='url_delete_order'),
    path('register/', views.register_view, name='url_register'),
    path('login/', views.login_view, name='url_login')
]
