from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="groups_created"
    )

    def __str__(self):
        return self.name


class Groupusers(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user.email} - {self.group.name}"
