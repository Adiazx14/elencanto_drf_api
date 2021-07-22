from store.serializers import CategorySerializer, ProductSerializer
from store.models import Category, Product
from rest_framework.generics import ListAPIView


class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
