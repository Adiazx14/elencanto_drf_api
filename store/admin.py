from .models import Category, Order, OrderItem, Product, ProductImage, ShippingAddress
from django.contrib import admin


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderItemInline,
    ]


class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [ProductImageInline]


# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ShippingAddress)
