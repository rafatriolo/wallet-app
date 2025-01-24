from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Modelo personalizado para o usuário."""

    email = models.EmailField(unique=True)
    # Ajuste os related_name para evitar conflitos
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
