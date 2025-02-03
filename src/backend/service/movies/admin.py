from django.contrib import admin
from django.db.models import Avg
from inlines import ActorMovieInLine, DirectorMovieInLine, ReviewInLine
from movies.models import Movie


# TODO: Add avg grade (works, should be tested more?)
class MovieAdmin(admin.ModelAdmin):
    """Movie admin panel"""

    inlines = [DirectorMovieInLine, ActorMovieInLine, ReviewInLine]
    list_display = [
        "title",
        "description",
        "get_directors",
        "average_rating_display",
        "id",
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

    def average_rating_display(self, obj):
        # Возвращаем округленное значение или "N/A" если оценка отсутствует
        return obj.average_rating

    average_rating_display.short_description = "Average Rating"


admin.site.register(Movie, MovieAdmin)
