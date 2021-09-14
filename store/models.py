from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey, OneToOneField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    countInStock = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, Category: {self.category}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = ImageField(null=True, blank=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    shipping_price = models.DecimalField(max_digits=7,
                                         decimal_places=2,
                                         blank=True,
                                         null=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    is_approved = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at} by {self.user}"


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField(blank=True, null=True, default=1)
    name = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=7,
                                decimal_places=2,
                                null=True,
                                blank=True)
    image = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return str(self.product) + " in Order: " + str(self.order)


class ShippingAddress(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             blank=True,
                             null=True)
    address = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=300, blank=True)
    zipcode = models.CharField(max_length=300, blank=True)
    state = models.CharField(max_length=100, blank=True)
    shipping_price = models.DecimalField(decimal_places=2,
                                         max_digits=7,
                                         blank=True,
                                         null=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.address + " (" + self.user.username + ")"
