from django.contrib import admin

from directors.models import Director
from movies.inlines import DirectorMovieInLine


class DirectorAdmin(admin.ModelAdmin):
    inlines = [
        DirectorMovieInLine,
    ]
    list_display = [
        "last_name",
        "first_name",
        "id",
    ]
    empty_value_display = "N/A"

    class Meta:
        model = Director
        fields = ["last_name", "first_name", "second_name"]


admin.site.register(Director, DirectorAdmin)
