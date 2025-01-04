from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Not returned in the response
    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = UserModel
        fields = [
            'username',
            'email',
            'password'
        ]
    
    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        # In order to hash the password
        return user