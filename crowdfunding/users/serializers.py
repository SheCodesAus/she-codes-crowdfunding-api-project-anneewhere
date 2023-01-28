from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password



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
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = { #kwargs= keyword arguments
            'password': {'write_only':True},
            'email': {'allow_blank':True, 'required':True}
            }

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user #returned the defined user.

class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True,write_only=True)
    new_password = serializers.CharField(required=True,write_only=True)

    def validate_old_password(self, value):
        if self.instance.check_password(value):
            return value
        raise serializers.ValidationError('Wrong password.')

    def update(self, instance, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save()
        return instance