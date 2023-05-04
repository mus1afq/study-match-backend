# Function to create a new URL pattern.
from django.urls import path

# Refers to the views module in the studymatch Django application directory
# containing functions that handle HTTP requests, which are matched with URLs in this file.
from studymatch import views

urlpatterns = [
    # A URL pattern to view user details for a specific user identified by their primary key (pk).
    path("user/<int:pk>", views.UserDetail.as_view(), name="user_detail"),
    # A URL pattern to create a new User object.
    path(
        "createuser/",
        views.CreateUserDetail.as_view(),
        name="Createuser_detail",
    ),
    # A URL pattern to create a new Group object.
    path(
        "create/group/",
        views.CreateGroupView.as_view(),
        name="create_group",
    ),
    # A URL pattern to join an existing group, identified by its primary key.
    path(
        "join/group/<int:group_id>/",
        views.JoinGroupView.as_view(),
        name="join_group",
    ),
    # A URL pattern to list all groups a user belongs to.
    path(
        "user/groups/",
        views.UserGroupListView.as_view(),
        name="user_groups",
    ),
    # A URL pattern to list all available groups.
    path(
        "groups/",
        views.GroupsListView.as_view(),
        name="groups",
    ),
]
