from django.urls import path
from .views import CategoriesView

urlpatterns = [
    path('categories/', view=CategoriesView.as_view())
]
