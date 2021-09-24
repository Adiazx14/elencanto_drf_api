from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.views import APIView, Response
from store.serializers import CategorySerializer, ProductSerializer
from store.models import Category, Product
from rest_framework.generics import ListAPIView


class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsView(ListAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer


class ProductDetail(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist():
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductsByCategory(APIView):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
