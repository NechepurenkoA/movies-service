from django.core.validators import RegexValidator
from rest_framework import serializers

from profiles.models import Profile, TelegramUser


class TelegramUserSerializer(serializers.ModelSerializer):
    """Serializer for TelegramUser model"""

    username = serializers.SerializerMethodField()

    class Meta:
        model = TelegramUser
        fields = "__all__"
        read_only_fields = [
            "username",
        ]

    def get_username(self, obj):
        return obj.profile.username


class ProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r"^[\w-]+$",
                message=(
                    "Переданное значение не соответствует данному усл.: "
                    "- буквы в диапазоне a-z A-Z "
                    "- знаки: -,_ "
                ),
                code="invalid_username",
            )
        ],
    )

    class Meta:
        model = Profile
        fields = ("username",)
