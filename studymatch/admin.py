from django.contrib import admin
from .models import Group, Groupusers

# Register your models here.

admin.site.register(Group)
admin.site.register(Groupusers)
