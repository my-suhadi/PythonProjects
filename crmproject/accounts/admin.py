from django.contrib import admin

# Register your models here.
from .models import Customer, Product, Order, Tag


# admin.site.register(Customer)
# admin.site.register(Product)
# admin.site.register(Order)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'status')
