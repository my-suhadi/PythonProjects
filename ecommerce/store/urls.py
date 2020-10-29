from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name='store_url'),
    path('cart/', views.cart, name='cart_url'),
    path('checkout/', views.checkout, name='checkout_url'),
]
