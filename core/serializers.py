from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers


# def username_validator(username):
#     if not any(char.isdigit() for char in username):
#         raise serializers.ValidationError("Should be a least one digit")


class CreateUserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=25, validators=[username_validator])
    class Meta:
        model = User
        fields = ("username", "password")

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return User.objects.create(**validated_data)

    def validate_password(self, password):
        if password.islower():
            raise serializers.ValidationError("Should be a least one upper case")
        return password

    def validate_username(self, username):
        if not any(char.isdigit() for char in username):
            raise serializers.ValidationError("Should be a least one digit")
        return username


class UserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=150, validators=[username_validator])

    class Meta:
        model = User
        fields = ("username", "date_joined", "last_login")
