from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from actors.api_views import ActorViewSet

router = DefaultRouter()
router.register(r"actors", ActorViewSet, basename="actors")

urlpatterns = [
    path(f"{settings.API_V1_PREFIX}/", include(router.urls)),
]
