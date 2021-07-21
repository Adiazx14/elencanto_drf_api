from django.urls import path
from .views import CategoriesView, ProductsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('categories/', view=CategoriesView.as_view()),
    path('products/', view=ProductsView.as_view())

]
