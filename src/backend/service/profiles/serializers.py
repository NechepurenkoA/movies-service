from rest_framework import serializers

from profiles.models import Profile, TelegramUser


class TelegramUserSerializer(serializers.ModelSerializer):
    """Serializer for TelegramUser model"""

    class Meta:
        model = TelegramUser
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):

    telegram_account = TelegramUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = (
            "username",
            "telegram_account",
        )
