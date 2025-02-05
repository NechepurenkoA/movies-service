from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from movies.api_views import MovieViewSet

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movies")

urlpatterns = [
    path(f"{settings.API_V1_PREFIX}/", include(router.urls)),
]
