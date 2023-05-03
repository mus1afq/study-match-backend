from django.urls import path
from studymatch import views

urlpatterns = [
    path("user/<int:pk>", views.UserDetail.as_view(), name="user_detail"),
    path(
        "createuser/",
        views.CreateUserDetail.as_view(),
        name="Createuser_detail",
    ),
    path(
        "create/group/",
        views.CreateGroupView.as_view(),
        name="create_group",
    ),
    path(
        "join/group/<int:group_id>/",
        views.JoinGroupView.as_view(),
        name="join_group",
    ),
]
