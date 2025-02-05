from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from profiles.api_views import ProfileViewSet, TelegramUserViewSet

router = DefaultRouter()
router.register(r"users", TelegramUserViewSet, basename="users")
router.register(r"profiles", ProfileViewSet, basename="profiles")

urlpatterns = [
    path(f"{settings.API_V1_PREFIX}/", include(router.urls)),
]
