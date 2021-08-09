from django.urls import path
from store.views import order_views as views

urlpatterns = [
    path('', view=views.Orders.as_view()),
    path("shipping/", view=views.ShippingAddressView.as_view()),
    path('<int:id>/', view=views.OrderDetail.as_view()),
    path('user/', view=views.UserOrders.as_view())
]
