from http import HTTPMethod

from rest_framework import mixins, viewsets

from profiles.models import Profile, TelegramUser
from profiles.serializers import ProfileSerializer, TelegramUserSerializer

# from profiles.permissions import IsBotOrAdmin


class TelegramUserViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    # permission_classes = (IsBotOrAdmin,)


class ProfileViewSet(
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Profile.objects.all()
    lookup_field = "telegram_account__telegram_id"
    serializer_class = ProfileSerializer
    # permission_classes = (IsBotOrAdmin,)
    http_method_names = [
        HTTPMethod.PATCH.lower(),
    ]
