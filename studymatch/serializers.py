# The built-in Django authentication user model, which is used for user authentication and authorization.
from django.contrib.auth.models import User

# Provides a powerful framework for serializing and deserializing data in Django.
# It includes an implementation of Django's ModelSerializer that makes it easy to convert Django model instances into JSON format.
from rest_framework import serializers

# A helper function provided by Django used to create a hashed password.
from django.contrib.auth.hashers import make_password

# Models defined in the application that are used by serializers to convert Python class objects into JSON format.
from .models import Group, Groupusers


# This serializer is used to serialize instances of the built-in Django User model. It inherits from serializers.ModelSerializer.
# Meta class specifies the model and fields to include in the serialized output.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username"]


# This serializer is used to create new user instances. It inherits from serializers.ModelSerializer.
# Meta class specifies the model and fields to include in the serialized input/output.
# It overrides the create method to hash password and save user object with that hashed password.
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


# This serializer is used to serialize instances of the custom Group model. It again inherits from serializers.ModelSerializer.
#  It adds a custom group_size field that counts the number of users in a group using get_group_size method defined in the same serializer.
class GroupSerializer(serializers.ModelSerializer):
    group_size = serializers.SerializerMethodField()
    # By default, ModelSerializer only includes fields that are actual fields on the model,
    # but we can specify additional fields using this serializer field.
    # get_group_size function then calculates the count of related objects via a reverse relationship.

    class Meta:
        model = Group
        fields = ["id", "name", "location", "group_date", "group_size"]

    def get_group_size(self, obj):
        """Return number of users in group."""
        return obj.groupusers_set.count()


# This serializer is used to serialize instances of the custom Groupusers model. It again inherits from serializers.ModelSerializer.
# The __all__ value for fields specifies that all fields from the model should be included in the serialized output.
class GroupusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupusers
        fields = "__all__"
