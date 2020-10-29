from django.shortcuts import render

# Create your views here.
from store.models import Product, Order


def store(request):
    all_products = Product.objects.all()
    cx = {
        'key_all_products': all_products
    }

    return render(request, 'store/store.html', cx)


def get_customer_data(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {
            'get_cart_items': 0,
            'get_cart_total': 0
        }

    cx = {
        'key_items': items,
        'key_order': order
    }

    return cx


def cart(request):
    return render(request, 'store/cart.html', get_customer_data(request))


def checkout(request):
    return render(request, 'store/checkout.html', get_customer_data(request))
