from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Group, Groupusers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username"]


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        """Hash password before saving user obj."""
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.password = make_password(password)
        user.save()
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name", "location"]


class GroupusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupusers
        fields = "__all__"
