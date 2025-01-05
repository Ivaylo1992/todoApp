from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate
from todoApp.accounts.serializers import (
    UserSerializer,
    LoginRequestSerializer,
    LoginResponseSerializer,
    LogoutRequestSerializer,
)
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

UserModel = get_user_model()

class RegisterView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@extend_schema(
    tags=['auth'],
    summary='Login endpoint',
    description='Authenticate user and get back acces and refresh tokens',
    request=LoginRequestSerializer,
    responses={
        200: LoginResponseSerializer,
        400: 'Invalid username or password'
    }
)

class LoginView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user is None:
            return Response(
                {
                'error': 'Invalid username or password'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'refresh': str(refresh),
                'acces': str(refresh.access_token),
                'message': 'Login successful',
            }, 
            status=status.HTTP_200_OK,
        )


@extend_schema(
    tags=['auth'],
    summary='Logout endpoint',
    description='Blacklist the refresh token',
    request=LogoutRequestSerializer,
    responses={
        200: LoginResponseSerializer,
        400: 'Invalid or expired token'
    }
)

class LogoutAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {
                    'message': 'Logout successful',
                },
                status=status.HTTP_200_OK,
            )
        except TokenError:
            return Response(
                {
                    'error': 'Invalid or expired token',
                },
                status=status.HTTP_400_BAD_REQUEST
            )