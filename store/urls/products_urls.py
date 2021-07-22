from django.urls import path
from store.views import products_views as views

urlpatterns = [

    path('categories/', view=views.CategoriesView.as_view()),
    path('', view=views.ProductsView.as_view())

]
