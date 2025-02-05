from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from actors.serializers import ActorSerializer
from directors.serializers import DirectorSerializer
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Serializer for Director model"""

    actors = ActorSerializer(many=True)
    directors = DirectorSerializer(many=True)
    image = Base64ImageField()

    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = ("slug",)
