from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .serializers import CustomTokenObtainSerializer, UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.views import APIView


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user_response = super().create(request, *args, **kwargs)
        user = User.objects.get(email=user_response.data['email'])
        token = AccessToken.for_user(user)
        return Response({'user': user_response.data, 'token': str(token)})


class LoginView(TokenViewBase):
    serializer_class = CustomTokenObtainSerializer


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = UserSerializer(request.user).data
        return Response({'user': data})
