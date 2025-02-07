from django.contrib import admin

from movies.models import Movie
from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "author__profile__username", "movie", "text", "rating"]
    readonly_fields = ["author", "movie", "text", "rating"]
    empty_value_display = "N/A"

    class Meta:
        model = Movie
        fields = ["author", "movie", "text", "rating"]

    def get_username(self, obj):
        return obj.author.profile.username

    def get_queryset(self, request):
        return Review.objects.all().select_related("author__profile", "movie")


admin.site.register(Review, ReviewAdmin)
