from django.contrib import admin
from movies.models import Movie
from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "author__profile__username", "movie", "text", "rating"]
    empty_value_display = "N/A"

    class Meta:
        model = Movie
        fields = ["author", "movie", "text", "rating"]


admin.site.register(Review, ReviewAdmin)
