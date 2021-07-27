from .models import Category, Order, OrderItem, Product, ShippingAddress
from django.contrib import admin


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderItemInline,
    ]


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
