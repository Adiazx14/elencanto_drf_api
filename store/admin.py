from .models import Category, Order, OrderItem, Product
from django.contrib import admin

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
