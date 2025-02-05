from rest_framework import mixins, pagination, viewsets

from directors.models import Director
from directors.serializers import DirectorSerializer

# from profiles.permissions import IsBotOrAdmin


class AbstractViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """Abstract class for Directors, Actors and Movies models"""

    # permission_classes = IsBotOrAdmin
    pagination_class = pagination.PageNumberPagination


class DirectorViewSet(AbstractViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
