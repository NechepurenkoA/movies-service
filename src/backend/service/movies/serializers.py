from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from actors.serializers import MovieActorRepresentationSerializer
from directors.serializers import MovieDirectorRepresentationSerializer
from movies.models import Movie


class MovieRepresentationSerializer(serializers.ModelSerializer):
    """Representation serializer for 'Movie' model."""

    image = Base64ImageField(required=False)
    actors = MovieActorRepresentationSerializer(many=True)
    directors = MovieDirectorRepresentationSerializer(many=True)
    average_grade = serializers.FloatField(read_only=True)

    def get_reviews_amount(self, obj) -> int:
        return obj.reviews.count()

    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = ("slug",)
