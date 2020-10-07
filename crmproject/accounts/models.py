from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
    )

    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=200, choices=CATEGORY)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('out of delivery', 'Out of delivery'),
        ('delivered', 'Devlivered'),
    )

    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)
