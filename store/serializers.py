from django.db.models import fields
from .models import Product
from .models import Category
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'icon']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
