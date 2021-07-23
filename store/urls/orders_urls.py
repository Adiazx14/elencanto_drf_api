from django.urls import path
from store.views import order_views as views

urlpatterns = [

    path('', view=views.Orders.as_view()),


]
