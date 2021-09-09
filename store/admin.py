from .models import Category, Order, OrderItem, Product, ProductImage, ShippingAddress
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class OrderItemInline(admin.TabularInline):
    model = OrderItem


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ShippingAdressInline(admin.TabularInline):
    model = ShippingAddress


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemInline, ShippingAdressInline]


class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [ProductImageInline]


# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ShippingAddress)
admin.site.register(Order, OrderAdmin)

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('My site admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('My administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administratin')

admin_site = MyAdminSite()