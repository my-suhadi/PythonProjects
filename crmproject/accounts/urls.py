from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='url_home'),
    path('products/', views.products, name='url_product'),
    path('customer/<str:customer_id>/', views.customer, name='url_customer'),
    path('account/', views.account_settings, name='url_account'),
    path('create_order/<str:customer_id>/', views.create_order, name='url_create_order'),
    path('update_order/<str:order_id>/', views.update_order, name='url_update_order'),
    path('delete_order/<str:order_id>/', views.delete_order, name='url_delete_order'),
    path('register/', views.register_user, name='url_register'),
    path('login/', views.login_user, name='url_login'),
    path('logout/', views.logout_user, name='url_logout'),
    path('user/', views.user_page, name='url_user_page')
]
