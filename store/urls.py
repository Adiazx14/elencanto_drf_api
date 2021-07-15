from django.urls import path
from .views import CategoriesView, ProductsView

urlpatterns = [
    path('categories/', view=CategoriesView.as_view()),
    path('products/', view=ProductsView.as_view())

]
