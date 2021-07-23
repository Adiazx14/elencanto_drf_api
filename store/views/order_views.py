from store.serializers import OrderSerializer
from store.models import Order, OrderItem, Product, ShippingAddress
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class Orders(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        order_items = data['order_items']

        if order_items and len(order_items == 0):
            return Response({"message": "There are no items"}, status=status.HTTP_400_BAD_REQUEST)

        else:
            order = Order.objects.create(
                user=user,
                shipping_price=data["shipping_price"],
                total_price=data["total_price"],
                payment_method=data['payment_method'],

            )

            ShippingAddress.objects.create(
                order=order,
                address=data['shipping_address']['address'],
                city=data['shipping_address']['city'],
                zipcode=data['shipping_address']['zipcode'],
            )

        for i in order_items:
            product = Product.objects.get(id=i["product"])

            item = OrderItem.objects.create(
                product=product,
                user=user,
                qty=data['qty'],
                image=data['product.image.url'],
                price=data['price']
            )

            product['countInStock'] -= item.qty
            product.save()

            serializer = OrderSerializer(order)
            return Response(serializer.data)

    def get(self, request):
        orders = Order.objects.all()
        order = Order.objects.get(id=2)
        print(order.shippingaddress)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderDetail(APIView):

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
