from actors.models import Actor
from actors.serializers import ActorSerializer
from directors.api_views import AbstractViewSet

# from profiles.permissions import IsBotOrAdmin


class ActorViewSet(AbstractViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
