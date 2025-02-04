from django.contrib import admin
from django.db.models import Avg

from movies.inlines import ActorMovieInLine, DirectorMovieInLine
from movies.models import Movie
from reviews.inlines import ReviewInLine


# TODO: Add avg grade (works, should be tested more?)
class MovieAdmin(admin.ModelAdmin):
    """Movie admin panel"""

    inlines = [DirectorMovieInLine, ActorMovieInLine, ReviewInLine]
    list_display = [
        "title",
        "description",
        "get_directors",
        "get_average_rating",
        "id",
    ]
    readonly_fields = [
        "slug",
    ]
    empty_value_display = "N/A"

    class Meta:
        model = Movie
        fields = [
            "title",
            "description",
            "directors",
            "actors",
            "release_date",
            "genre",
        ]

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .annotate(average_rating=Avg("reviews__rating"))
        )

    def get_directors(self, obj):
        return [str(_.director) for _ in obj.directors.all()]

    get_directors.short_description = "Directors"

    def get_average_rating(self, obj):
        # Возвращаем округленное значение или "N/A" если оценка отсутствует
        return obj.average_rating

    get_average_rating.admin_order_field = "average_rating"
    get_average_rating.short_description = "Average Rating"


admin.site.register(Movie, MovieAdmin)
