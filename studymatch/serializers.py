from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Group, Groupusers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username"]


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class GroupusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupusers
        fields = "__all__"
