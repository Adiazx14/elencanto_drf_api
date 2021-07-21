from .serializers import CategorySerializer, ProductSerializer, MyTokenObtainPairSerializer
from .models import Category, Product
from django.http import HttpResponse
from rest_framework.views import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import status
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
