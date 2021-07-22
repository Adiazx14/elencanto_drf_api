from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from store.serializers import MyTokenObtainPairSerializer, UserSerializer, UserSerializerWithToken
from rest_framework.views import APIView, Response
from rest_framework.views import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data

        try:
            user = User.objects.create(
                first_name=data["name"],
                email=data['email'],
                username=data['email'],
                password=make_password(data['password'])
            )
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


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
