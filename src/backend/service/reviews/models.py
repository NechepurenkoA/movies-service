from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from movies.models import Movie
from profiles.models import TelegramUser
from reviews.constants import ReviewRestrictions


class Review(models.Model):
    """Review model, mid-model (table) relation between movie and user for reviews"""

    author = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField(max_length=500, default="")
    rating = models.IntegerField(
        default=ReviewRestrictions.DEFAULT_REVIEW_GRADE,
        validators=[
            MinValueValidator(ReviewRestrictions.MIN_REVIEW_GRADE),
            MaxValueValidator(ReviewRestrictions.MAX_REVIEW_GRADE),
        ],
    )
    add_date = models.DateTimeField(auto_now_add=True)
