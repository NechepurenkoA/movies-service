from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from directors.api_views import DirectorViewSet

router = DefaultRouter()
router.register(r"directors", DirectorViewSet, basename="directors")

urlpatterns = [
    path(f"{settings.API_V1_PREFIX}/", include(router.urls)),
]
