from django.contrib.auth.models import User
from django.db import models


class TelegramUser(models.Model):
    """Telegram user model"""

    telegram_id = models.CharField(unique=True, max_length=9)
    activation_date = models.DateTimeField(
        auto_now_add=True
    )  # Will be implemented later on for code authorization on site


class Profile(models.Model):
    """Profile model"""

    username = models.CharField(
        verbose_name="Username to show",
        unique=False,
        max_length=20,
        default="User.username",
    )
    telegram_account = models.OneToOneField(
        TelegramUser, on_delete=models.CASCADE, related_name="profile"
    )
    user_account = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )  # Will be implemented later on for site development
