from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    # groups = models.ManyToManyField(
    #     Group,
    #     related_name="custom_user_groups",
    #     blank=True,
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name="custom_user_permissions",
    #     blank=True,
    # )
    pass