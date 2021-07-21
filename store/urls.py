from django.urls import path
from .views import CategoriesView, ProductsView, MyTokenObtainPairView, UserView

urlpatterns = [
    path('user/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/profile/', UserView.as_view()),
    path('categories/', view=CategoriesView.as_view()),
    path('products/', view=ProductsView.as_view())

]
