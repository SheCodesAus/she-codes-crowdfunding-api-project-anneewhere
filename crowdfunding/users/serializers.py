from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    profile_picture = serializers.URLField(blank=True, null=True)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'email', 'profile_picture', 'password']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        return CustomUser

class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)