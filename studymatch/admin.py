from django.contrib import (
    admin,
)  # This imports the admin module for the Django project.
from .models import (
    Group,
    Groupusers,
)  # This imports the Group and Groupusers models from the models.py file in the current directory (indicated by the ".").

# Register your models here.

# This registers the Group model with the admin site so that it can be viewed, added, edited, and deleted through the Django Admin interface.
admin.site.register(Group)
# This registers the Groupusers model with the admin site so that it can be viewed, added, edited, and deleted through the Django Admin interface.
admin.site.register(Groupusers)
