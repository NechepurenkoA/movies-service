from rest_framework import serializers

from directors.models import Director
from movies.models import MovieDirector


class DirectorSerializer(serializers.ModelSerializer):
    """Serializer for Director model"""

    class Meta:
        model = Director
        fields = "__all__"


class MovieDirectorRepresentationSerializer(serializers.ModelSerializer):

    director = DirectorSerializer()

    class Meta:
        model = MovieDirector
        fields = ("director",)
