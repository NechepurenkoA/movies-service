from django.contrib import admin

from reviews.models import Review


class ReviewInLine(admin.TabularInline):
    """Reviews admin panel inline"""

    model = Review
    extra = 1
    readonly_fields = ["author", "add_date", "text", "rating", "movie"]
