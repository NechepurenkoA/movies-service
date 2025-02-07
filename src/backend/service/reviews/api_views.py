from http import HTTPMethod

from rest_framework import mixins, permissions

from directors.api_views import AbstractViewSet
from reviews.models import Review
from reviews.serializers import (
    ReviewRepresentationSerializer,
    ReviewSerializer,
    ReviewUpdateSerializer,
)

# from profiles.permissions import IsBotOrAdmin


class ReviewViewSet(
    AbstractViewSet, mixins.DestroyModelMixin, mixins.RetrieveModelMixin
):
    queryset = Review.objects.all().select_related("movie", "author__profile")
    serializer_class = ReviewRepresentationSerializer
    http_method_names = [
        HTTPMethod.GET.lower(),
        HTTPMethod.POST.lower(),
        HTTPMethod.PATCH.lower(),
        HTTPMethod.DELETE.lower(),
    ]

    def get_serializer_class(self):
        if self.request.method == HTTPMethod.PATCH:
            return ReviewUpdateSerializer
        if self.request.method not in permissions.SAFE_METHODS:
            return ReviewSerializer
        return super().get_serializer_class()
