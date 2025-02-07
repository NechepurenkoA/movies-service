from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from reviews.api_views import ReviewViewSet

router = DefaultRouter()
router.register(r"reviews", ReviewViewSet, basename="reviews")

urlpatterns = [
    path(f"{settings.API_V1_PREFIX}/", include(router.urls)),
]
