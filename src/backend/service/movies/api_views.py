from http import HTTPMethod

from django.db.models import Avg
from rest_framework import filters, mixins
from rest_framework.decorators import action

from directors.api_views import AbstractViewSet
from movies.models import Movie
from movies.serializers import MovieRepresentationSerializer
from reviews.models import Review
from reviews.serializers import ReviewRepresentationSerializer

# from profiles.permissions import IsBotOrAdmin


class MovieViewSet(
    AbstractViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = MovieRepresentationSerializer
    lookup_field = "slug"
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = [
        "slug",
        "title",
        "directors__director__last_name",
        "genre",
    ]
    ordering_fields = [
        "id",
        "average_grade",
        "slug",
        "title",
    ]
    ordering = [
        "average_grade",
    ]
    http_method_names = [
        HTTPMethod.GET.lower(),
    ]

    def get_queryset(self):
        queryset = Movie.objects.prefetch_related(
            "actors__actor", "directors__director"
        ).annotate(average_grade=Avg("reviews__rating"))
        return queryset

    @action(
        methods=["get"],
        detail=True,
        serializer_class=ReviewRepresentationSerializer,
        url_path="reviews",
    )
    def get_reviews(self, request, slug):
        queryset = (
            Review.objects.select_related("movie", "author__profile")
            .filter(movie__slug=slug)
            .order_by("add_date")
        )
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
