from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from django.http import HttpResponse
from rest_framework.views import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import status

# Create your views here.


class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
