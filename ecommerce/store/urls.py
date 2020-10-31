from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name='storeUrl'),
    path('cart/', views.cart, name='cartUrl'),
    path('checkout/', views.checkout, name='checkoutUrl'),
    path('update-item/', views.update_item, name='updateItemUrl'),
]
