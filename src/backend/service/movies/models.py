from actors.models import Actor
from directors.models import Director
from django.db import models
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    """Movie model"""

    class Genres(models.TextChoices):
        HORROR = "horror", _("Horror")
        ROMANCE = "romance", _("Romance")
        COMEDY = "comedy", _("Comedy")
        ACTION = "action", _("Action")
        SCI_FI = "sci-fi", _("Sci-Fi")

    title = models.CharField(
        verbose_name="Title",
        max_length=75,
    )
    slug = models.SlugField(max_length=75, unique=True)
    description = models.TextField(max_length=500)
    release_date = models.DateField(blank=False)
    genre = models.CharField(choices=Genres.choices, max_length=15, blank=False)

    def __str__(self):
        return self.title


class MovieActor(models.Model):
    """A mid-model (table) between movie and actors relation"""

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="actors",
    )
    actor = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
        related_name="movies",
    )
    role = models.CharField(default="Unknown", max_length=15)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["movie", "actor", "role"],
                name="uniquetogether_movie_actor_role",
            )
        ]


class MovieDirector(models.Model):
    """A mid-model (table) between movie and director relation"""

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="directors",
    )
    director = models.ForeignKey(
        Director, on_delete=models.SET_DEFAULT, default="Unknown", related_name="movies"
    )

    class Meta:
        unique_together = ("movie", "director")
