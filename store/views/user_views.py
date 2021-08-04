from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from store.serializers import MyTokenObtainPairSerializer, UserSerializer, UserSerializerWithToken
from rest_framework.views import APIView, Response
from rest_framework.views import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserRegister(APIView):
    def post(self, request):
        data = request.data

        try:
            user = User.objects.create(first_name=data["first_name"],
                                       last_name=data["last_name"],
                                       email=data['email'],
                                       username=data['email'],
                                       password=make_password(
                                           data['password']))
            serializer = UserSerializerWithToken(user)
            return Response(serializer.data)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        data = request.data

        serializer = UserSerializerWithToken(user)

        user.password = make_password(data['password'])
        user.save()
        return (Response(serializer.data))


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
