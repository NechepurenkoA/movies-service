from rest_framework import filters, mixins

from directors.api_views import AbstractViewSet
from movies.models import Movie
from movies.serializers import MovieSerializer

# from profiles.permissions import IsBotOrAdmin


class MovieViewSet(
    AbstractViewSet,
    mixins.ListModelMixin,
):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "slug"
    filter_backends = (filters.SearchFilter,)
    search_filter = ("slug", "title", "directors")
