from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# uuid sebagai id
# https://dev.to/serhatteker/how-to-use-uuid-as-a-primary-id-in-django-models-4bhc


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    digital = models.BooleanField(default=False)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.image.url
        except ValueError:
            url = 'static/images/placeholder.png'
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=255)

    def __str__(self):
        return '{}. {}'.format(self.id, self.transaction_id)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum(item.get_total for item in order_items)
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum(item.quantity for item in order_items)
        return total

    @property
    def shipping(self):
        shipping_ = False
        order_items = self.orderitem_set.all()
        for i in order_items:
            if not i.product.digital:
                shipping_ = True

        return shipping_


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}. {}'.format(self.id, self.product.name)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=6)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}. {}'.format(self.customer.name, self.address)
