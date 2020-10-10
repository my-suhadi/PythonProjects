from django.shortcuts import render, redirect

# Create your views here.
from .models import Product, Order, Customer
from .form import OrderForm


def home(request):
    all_order = Order.objects.all()
    all_customer = Customer.objects.all()

    total_order = all_order.count()

    delivered = all_order.filter(status='delivered').count()
    pending = all_order.filter(status='pending').count()

    cx = {
        'key_order': all_order,
        'key_customer': all_customer,
        'key_total_order': total_order,
        'key_delivered': delivered,
        'key_pending': pending,
    }
    return render(request, 'accounts/dashboard.html', cx)


def products(request):
    all_product = Product.objects.all()
    cx = {
        'key_products': all_product
    }
    return render(request, 'accounts/products.html', cx)


def customer(request, customer_id):
    cust = Customer.objects.get(id=customer_id)
    customer_order = cust.order_set.all()

    cx = {
        'key_customer': cust,
        'key_customer_order': customer_order
    }

    return render(request, 'accounts/customer.html', cx)


def create_order(request):
    order_form = OrderForm()

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('/')

    cx = {
        'key_order_form': order_form
    }

    return render(request, 'accounts/create_order.html', cx)


def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order_form = OrderForm(instance=order)

    if request.method == 'POST':
        order_form = OrderForm(request.POST, instance=order)
        if order_form.is_valid():
            order_form.save()
            return redirect('/')

    cx = {
        'key_order_form': order_form
    }
    return render(request, 'accounts/create_order.html', cx)


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    cx = {
        'key_order': order
    }
    return render(request, 'accounts/delete_order.html', cx)
