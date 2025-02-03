from django.contrib import admin
from movies.models import MovieActor, MovieDirector
from reviews.models import Review


class DirectorMovieInLine(admin.StackedInline):
    """Directors / Movies admin panel inline"""

    model = MovieDirector
    extra = 0


class ReviewInLine(admin.StackedInline):
    """Reviews admin panel inline"""

    model = Review
    extra = 1


class ActorMovieInLine(admin.StackedInline):
    """Actors / Movies admin panel inline"""

    model = MovieActor
    extra = 0
