import re
from django.db.models.fields import DateTimeCheckMixin
from store.serializers import OrderSerializer, ShippingAddressSerializer
from store.models import Order, OrderItem, Product, ShippingAddress
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, status
from datetime import datetime
from django.utils import timezone


class Orders(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        order_items = data['order_items']

        if order_items and len(order_items) == 0:
            return Response({"message": "There are no items"},
                            status=status.HTTP_400_BAD_REQUEST)

        else:
            order = Order.objects.create(
                user=user,
                total_price=data["total_price"],
            )

            ShippingAddress.objects.create(
                order=order,
                address=data['shipping_address']['street'],
                city=data['shipping_address']['city'],
                zipcode=data['shipping_address']['zipcode'],
                state=data['shipping_address']['state'],
            )

        for i in order_items:
            product = Product.objects.get(id=i["product"])

            item = OrderItem.objects.create(product=product,
                                            user=user,
                                            qty=i['qty'],
                                            image=i['image'],
                                            price=i['price'])

            product.countInStock -= item.qty
            product.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def get(self, request):
        user = request.user
        orders = user.order_set.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        user = request.user
        try:
            order = Order.objects.get(id=id)

            if order.user == user or user.is_staff:
                serializer = OrderSerializer(order)

                return Response(serializer.data)

            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            order = Order.objects.get(id=id)
            if request.data["action"] == "pay":
                order.is_paid = True
                order.paid_at = datetime.now(tz=timezone.utc)
            elif request.data["action"] == "deliver":
                order.is_delivered = True
                order.delivered_at = datetime.now(tz=timezone.utc)
            order.save()
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserOrders(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        orders = user.order_set.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class ShippingAddressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        addresses = request.user.shippingaddress_set.all()
        serializer = ShippingAddressSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        address = ShippingAddress.objects.create(user=request.user,
                                                 address=data['street'],
                                                 city=data["city"],
                                                 zipcode=data["zipcode"],
                                                 state=data["state"],
                                                 is_default=data["default"])

        serializer = ShippingAddressSerializer(address)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShippingAddressDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_address(self, id):
        try:
            address = ShippingAddress.objects.get(id=id)
            return address
        except ShippingAddress.DoesNotExist():
            return Response(status=status.HTTP_404_BAD_REQUEST)

    def get(self, request, id):
        address = self.get_address(id)
        serializer = ShippingAddressSerializer(address)
        return Response(serializer.data)

    def put(self, request, id):
        address = self.get_address(id)
        serializer = ShippingAddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        address = self.get_address(id)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
