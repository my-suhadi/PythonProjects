import datetime
import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from store.models import Product, Order, OrderItem, ShippingAddress


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items = order.get_cart_items

    else:
        order = {
            'get_cart_items': 0,
            'get_cart_total': 0,
            'shipping': False
        }
        cart_items = order['get_cart_items']

    all_products = Product.objects.all()
    cx = {
        'allProductsKey': all_products,
        'cartItemsKey': cart_items
    }

    return render(request, 'store/store.html', cx)


def cart(request):
    return render(request, 'store/cart.html', get_customer_data(request))


def checkout(request):
    return render(request, 'store/checkout.html', get_customer_data(request))


def get_customer_data(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

    else:
        items = []
        order = {
            'get_cart_items': 0,
            'get_cart_total': 0,
            'shipping': False
        }
        cart_items = order['get_cart_items']

    cx = {
        'itemsKey': items,
        'orderKey': order,
        'cartItemsKey': cart_items
    }

    return cx


def update_item(request):
    print(request.body)
    data = json.loads(request.body)
    print(data)

    product_id = data['productId']
    action = data['action']
    print('Action: ', action)
    print('Product ID: ', product_id)

    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = order_item.quantity + 1
    elif action == 'remove':
        order_item.quantity = order_item.quantity - 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('item was added', safe=False)


@csrf_exempt
def process_order(request):
    print('Data: ', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = data['form']['total']
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True

        order.save()

        if order.shipping:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zip_code=data['shipping']['zipcode']
            )
    else:
        print('user is not logged in')

    return JsonResponse('Payment submitted', safe=False)
