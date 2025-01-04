from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from todoApp.accounts.serializers import UserSerializer
from rest_framework.permissions import AllowAny


UserModel = get_user_model()

class RegisterView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]