from django.contrib import admin
from django.db.models import Avg
from django.utils.html import format_html

from movies.inlines import ActorMovieInLine, DirectorMovieInLine
from movies.models import Movie
from reviews.inlines import ReviewInLine


# TODO: Add avg grade (works, should be tested more?)
class MovieAdmin(admin.ModelAdmin):
    """Movie admin panel"""

    inlines = [DirectorMovieInLine, ActorMovieInLine, ReviewInLine]
    list_display = [
        "title",
        "preview_image",
        "description",
        "get_directors",
        "get_average_rating",
        "id",
    ]
    readonly_fields = [
        "slug",
        "preview_image",
    ]
    empty_value_display = "N/A"

    class Meta:
        model = Movie
        fields = [
            "image",
            "preview_image",
            "title",
            "description",
            "directors",
            "actors",
            "release_date",
            "genre",
        ]

    def get_queryset(self, request):
        """Function annotates avarage grade of the movies."""
        return (
            super()
            .get_queryset(request)
            .annotate(average_rating=Avg("reviews__rating"))
            .prefetch_related("directors__director", "actors")
            .distinct()
        )

    def preview_image(self, obj):
        """Function return a preview of the movie."""
        return format_html(
            f'<img src="{obj.image.url}" style="max-width:200px; max-height:200px"/>'
        )

    def get_directors(self, obj):
        """Function returns all directors of the movie as a list of strings."""
        return [str(_.director) for _ in obj.directors.all()]

    get_directors.short_description = "Directors"

    def get_average_rating(self, obj):
        # Возвращаем округленное значение или "N/A" если оценка отсутствует
        return obj.average_rating

    get_average_rating.admin_order_field = "average_rating"
    get_average_rating.short_description = "Average Rating"


admin.site.register(Movie, MovieAdmin)
