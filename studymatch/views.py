from django.contrib.auth.models import User
from studymatch.serializers import UserSerializer, CreateUserSerializer
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from studymatch.models import Group
from studymatch.serializers import GroupSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class CreateUserDetail(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]


class CreateGroupView(CreateAPIView):
    """API view to create a group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Set the group's creator to the logged in user."""
        serializer.save(creator=self.request.user)
