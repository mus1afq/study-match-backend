# This imports the Django models package, which allows for the creation of database models.
from django.db import models

# This imports the built-in Django User model, which is used to represent user accounts in the application.
from django.contrib.auth.models import User


class Group(models.Model):
    # This creates a field named name with a maximum length of 20 characters, which will store the name of the group.
    name = models.CharField(max_length=20)
    # This creates a field named location with a maximum length of 20 characters, which will store the location of the group.
    location = models.CharField(max_length=20)
    # This creates a field named created_date of type DateTimeField with the current date/time set automatically when a new group is created.
    created_date = models.DateTimeField(auto_now_add=True)
    # This creates a foreign key relationship with the User model referenced by User model's primary key. It sets
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="groups_created"
    )
    # This creates a nullable field named group_date of type DateTimeField,
    # allowing for later assignment of the day and time of the group event.
    group_date = models.DateTimeField(null=True, blank=True)

    # This method defines a string representation for instances of the Group model.
    #  When an instance of this model is printed, it will return its name.
    def __str__(self):
        return self.name


class Groupusers(models.Model):
    # This creates a foreign key relationship with the Group model referenced by Group model's primary key.
    # It sets on_delete=models.CASCADE, which means that if a Group object referenced by a Groupusers
    # object's group attribute is deleted,all related Groupusers objects referencing it will be deleted as well.
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )
    # his creates a foreign key relationship with the User model referenced by User model's primary key. It sets
    # on_delete=models.CASCADE, which means that if a User object referenced by a Groupusers object's user
    # attribute is deleted, all related Groupusers objects referencing it will be deleted as well.
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    # This method defines a string representation for instances of the Groupusers model.When an instance of this
    # model is printed, it will return the email of its associated user and the name of the group.
    def __str__(self):
        return f"{self.user.email} - {self.group.name}"
