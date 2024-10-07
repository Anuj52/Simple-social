from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.utils import timezone
from groups.models import Group

class User(AbstractUser):
    # your custom fields and methods
    
    # specify unique related_name for groups and user_permissions fields
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')