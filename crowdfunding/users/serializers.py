from rest_framework import serializers
from .models import CustomUser


# class CustomUserSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     name = serializers.CharField(max_length=100)
#     username = serializers.CharField(max_length=50)
#     email = serializers.EmailField()
#     profile_picture = serializers.URLField()

#     def create(self, validated_data):
#         return CustomUser.objects.create(**validated_data)

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'name', 'email', 'profile_picture', 'password']
        extra_kwargs = { #kwargs= keyword arguments
            'password': {'write_only':True},
            'email': {'allow_blank':True, 'required':True}
            }

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user #returned the defined user.

class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)