from django.contrib import admin

from movies.models import MovieActor, MovieDirector


class DirectorMovieInLine(admin.StackedInline):
    """Directors / Movies admin panel inline"""

    model = MovieDirector
    extra = 0


class ActorMovieInLine(admin.StackedInline):
    """Actors / Movies admin panel inline"""

    model = MovieActor
    extra = 0
