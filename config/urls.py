"""This imports the admin module for the Django project."""
from django.contrib import admin

""" This imports functions to define the URL patterns of the project."""
from django.urls import path, include

"""This imports three views used to obtain, refresh or verify JWT tokens."""
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path(
        # This sets up this endpoint to access the Django Admin interface.
        "admin/",
        admin.site.urls,
    ),
    path(
        # This includes the urls.py file from another app called "studymatch".
        "",
        include("studymatch.urls"),
    ),
    path(
        # This sets up an endpoint for obtaining JWT tokens. When this endpoint is accessed with valid credentials, it returns a token that can be used for authentication.
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        # This sets up an endpoint for refreshing JWT tokens. When an authenticated user accesses this endpoint, it refreshes their token so they do not have to re-authenticate.
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        # This sets up an endpoint to verify whether a given token is valid or not.
        "api/token/verify/",
        TokenVerifyView.as_view(),
        name="token_verify",
    ),
]
"""These urlpatterns will be accessed when a user navigates to the corresponding URLs in the web application."""
