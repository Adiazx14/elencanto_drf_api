from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    icon = ImageField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    countInStock = models.IntegerField()
    createdAt = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return f"{self.name}, Category: {self.category}"
