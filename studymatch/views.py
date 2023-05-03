from django.contrib.auth.models import User
from rest_framework import status
from studymatch.serializers import UserSerializer, CreateUserSerializer
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    get_object_or_404,
    ListAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from studymatch.models import Group, Groupusers
from studymatch.serializers import GroupSerializer, GroupusersSerializer


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
        """Set the group's creator to the logged in user and add the user to the group."""
        group = serializer.save(creator=self.request.user)
        Groupusers.objects.create(user=self.request.user, group=group)


class JoinGroupView(CreateAPIView):
    serializer_class = GroupusersSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Get the group id from the url and create a Groupusers object
        with the group id and the logged in user.
        """
        group_id = kwargs.get("group_id")
        group = get_object_or_404(Group, id=group_id)
        user = request.user
        group_user = Groupusers.objects.filter(group=group, user=user).first()

        if group_user:
            return Response(
                {"detail": "You are already a member of this group"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.serializer_class(data={"group": group_id, "user": user.id})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"detail": "You have successfully joined the group"},
        )


class UserGroupListView(ListAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Group.objects.filter(groupusers__user=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class GroupsListView(ListAPIView):
    """
    API view to list all groups that the user is not a member of
    and allow the user to join them.
    """

    serializer_class = GroupSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Get the IDs of the groups that the user is already a member of and
        exclude them from the queryset.
        """
        user = self.request.user
        user_group_ids = user.groupusers_set.values_list("group__id", flat=True)
        queryset = Group.objects.exclude(id__in=user_group_ids)
        return queryset
