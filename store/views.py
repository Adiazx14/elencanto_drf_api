from .serializers import CategorySerializer, ProductSerializer, MyTokenObtainPairSerializer, UserSerializer
from .models import Category, Product
from django.http import HttpResponse
from rest_framework.views import APIView, Response
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


class UserView(APIView):

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
