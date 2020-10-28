from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

# Create your views here.
from .decorators import unauthenticated_user, allowed_user, admin_only
from .models import Product, Order, Customer
from .form import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter


@unauthenticated_user
def register_user(request):
    reg_form = CreateUserForm()

    if request.method == 'POST':
        reg_form = CreateUserForm(request.POST)
        if reg_form.is_valid():
            group = Group.objects.get(name='customer')

            user_reg = reg_form.save()
            user_reg.groups.add(group)

            Customer.objects.create(user=user_reg,
                                    name=reg_form.cleaned_data['username'],
                                    email=reg_form.cleaned_data['email'])

            messages.success(request, 'Account was created for ' + reg_form.cleaned_data.get('username'))
            return redirect('url_login')
        else:
            messages.error(request, reg_form.errors)
            return redirect('url_register')

    cx = {
        'key_reg_form': reg_form
    }
    return render(request, 'accounts/register.html', cx)


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        input_username = request.POST.get('username')
        input_password = request.POST.get('password')
        user_input = authenticate(request, username=input_username, password=input_password)

        if user_input is not None:
            login(request, user_input)
            return redirect('url_home')
        else:
            messages.info(request, 'Username or password is incorrect')

    cx = {}
    return render(request, 'accounts/login.html', cx)


def logout_user(request):
    logout(request)
    return redirect('url_login')


@login_required(login_url='url_login')
@allowed_user(allowed_group=['customer'])
def user_page(request):
    order_by_customer = request.user.customer.order_set.all()

    total_order = order_by_customer.count()
    delivered = order_by_customer.filter(status='delivered').count()
    pending = order_by_customer.filter(status='pending').count()

    cx = {
        'key_order_by_customer': order_by_customer,
        'key_total_order': total_order,
        'key_delivered': delivered,
        'key_pending': pending,
    }
    return render(request, 'accounts/user.html', cx)


@login_required(login_url='url_login')
@admin_only
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


@login_required(login_url='url_login')
@allowed_user(allowed_group=['customer'])
def account_settings(req):
    request_customer = req.user.customer
    form = CustomerForm(instance=request_customer)

    if req.method == 'POST':
        form = CustomerForm(req.POST, req.FILES, instance=request_customer)
        if form.is_valid():
            form.save()

    cx = {
        'key_form': form
    }
    return render(req, 'accounts/account_settings.html', cx)


@login_required(login_url='url_login')
@allowed_user(allowed_group=['admin'])
def products(request):
    all_product = Product.objects.all()
    cx = {
        'key_products': all_product
    }
    return render(request, 'accounts/products.html', cx)


@login_required(login_url='url_login')
@allowed_user(allowed_group=['admin'])
def customer(request, customer_id):
    customer_by_id = Customer.objects.get(id=customer_id)
    customer_order = customer_by_id.order_set.all()
    customer_order_count = customer_order.count()

    field_filter = OrderFilter(request.GET, queryset=customer_order)
    customer_order = field_filter.qs

    cx = {
        'key_customer': customer_by_id,
        'key_customer_order': customer_order,
        'key_customer_order_count': customer_order_count,
        'key_field_filter': field_filter
    }

    return render(request, 'accounts/customer.html', cx)


@login_required(login_url='url_login')
@allowed_user(allowed_group=['admin'])
def create_order(request, customer_id):
    current_customer = Customer.objects.get(id=customer_id)
    order_form_set = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)

    # order_form = OrderForm(initial={'customer': current_customer})
    formset = order_form_set(queryset=Order.objects.none(), instance=current_customer)

    if request.method == 'POST':
        # order_form = OrderForm(request.POST)
        formset = order_form_set(request.POST, instance=current_customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    cx = {
        'key_order_form': formset
    }

    return render(request, 'accounts/create_order.html', cx)


@login_required(login_url='url_login')
@allowed_user(allowed_group=['admin'])
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


@login_required(login_url='url_login')
def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    cx = {
        'key_order': order
    }
    return render(request, 'accounts/delete_order.html', cx)
