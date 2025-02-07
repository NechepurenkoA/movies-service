from rest_framework import serializers

from actors.models import Actor
from movies.models import MovieActor


class ActorSerializer(serializers.ModelSerializer):
    """Serializer for Director model"""

    class Meta:
        model = Actor
        fields = "__all__"


class MovieActorRepresentationSerializer(serializers.ModelSerializer):

    actor = ActorSerializer()

    class Meta:
        model = MovieActor
        fields = ("actor", "role")
        read_only_fields = ("actor", "role")
