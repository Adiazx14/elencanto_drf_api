from .serializers import CategorySerializer
from .models import Category
from django.http import HttpResponse
from rest_framework.views import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import status

# Create your views here.


class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
