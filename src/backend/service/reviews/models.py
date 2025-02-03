from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from movies.models import Movie


class Review(models.Model):
    """Review model, mid-model (table) relation between movie and user for reviews"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField(max_length=500, default="")
    rating = models.IntegerField(
        default=10, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    add_date = models.DateTimeField(auto_now_add=True)
