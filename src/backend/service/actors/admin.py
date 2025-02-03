from actors.models import Actor
from django.contrib import admin
from inlines import ActorMovieInLine


class ActorAdmin(admin.ModelAdmin):
    inlines = [
        ActorMovieInLine,
    ]
    list_display = [
        "last_name",
        "first_name",
        "get_movies",
        "id",
    ]
    empty_value_display = "N/A"

    class Meta:
        model = Actor
        fields = ["last_name", "first_name", "second_name"]

    def get_movies(self, obj):
        return [str(_.movie) for _ in obj.movies.all()]


admin.site.register(Actor, ActorAdmin)
