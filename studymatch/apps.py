from django.apps import (
    AppConfig,
)  # This imports the AppConfig module from the Django apps package.


class StudymatchConfig(
    AppConfig
):  # This defines a new class named StudymatchConfig that inherits from AppConfig.
    # This sets the default primary key field for models in the studymatch app to be a BigAutoField,
    # which is an automatically incrementing 64-bit integer field.
    default_auto_field = "django.db.models.BigAutoField"
    # This sets the name of the studymatch app, which should match the
    # name of the directory containing the app's models.py and views.py files.
    name = "studymatch"
