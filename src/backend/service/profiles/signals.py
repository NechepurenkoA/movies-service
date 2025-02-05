from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile, TelegramUser


@receiver(post_save, sender=TelegramUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            telegram_account=instance, username=f"User-{instance.id}"
        )
