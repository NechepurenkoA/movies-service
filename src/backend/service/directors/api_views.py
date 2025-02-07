from rest_framework import mixins, viewsets

from directors.models import Director
from directors.serializers import DirectorSerializer

# from profiles.permissions import IsBotOrAdmin


class AbstractViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """Abstract class for Directors, Actors and Movies models"""

    pass


class DirectorViewSet(AbstractViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
