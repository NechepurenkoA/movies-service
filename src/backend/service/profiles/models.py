from django.db import models


class TelegramUser(models.Model):
    """Telegram user model"""

    telegram_id = models.CharField(unique=True, max_length=9)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.telegram_id


class Profile(models.Model):
    """Profile model"""

    username = models.CharField(
        verbose_name="Username to show",
        unique=False,
        max_length=20,
    )
    telegram_account = models.OneToOneField(
        TelegramUser, on_delete=models.CASCADE, related_name="profile"
    )
