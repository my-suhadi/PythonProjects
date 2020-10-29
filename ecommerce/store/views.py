from django.shortcuts import render


# Create your views here.

def store(request):
    cx = {}
    return render(request, 'store/store.html', cx)


def cart(request):
    cx = {}
    return render(request, 'store/cart.html', cx)


def checkout(request):
    cx = {}
    return render(request, 'store/checkout.html', cx)
