from http import HTTPStatus

from django.shortcuts import get_object_or_404
from rest_framework import serializers, validators

from movies.models import Movie
from profiles.models import TelegramUser
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):

    telegram_user_id = serializers.CharField(required=True, write_only=True)
    movie = serializers.SlugRelatedField(
        slug_field="slug", queryset=Movie.objects.all()
    )

    class Meta:
        model = Review
        fields = [
            "id",
            "telegram_user_id",
            "author",
            "movie",
            "text",
            "rating",
        ]
        read_only_fields = [
            "author",
        ]

    def validate(self, attrs):
        if not TelegramUser.objects.filter(
            telegram_id=attrs["telegram_user_id"]
        ).exists():
            raise validators.ValidationError(
                {
                    "error": "Account is not registered. "
                    "Reviewing is not allowed. Please proceed to the "
                    "account registration in @reviewsonmoviesbot."
                },
                HTTPStatus.FORBIDDEN,
            )
        if Review.objects.filter(
            author__telegram_id=attrs["telegram_user_id"], movie=attrs["movie"]
        ).exists():
            raise validators.ValidationError(
                {"error": "You alredy made a review on this movie."},
                HTTPStatus.FORBIDDEN,
            )
        return attrs

    def create(self, validated_data):
        telegram_user = get_object_or_404(
            TelegramUser, telegram_id=validated_data.pop("telegram_user_id")
        )
        instance = Review.objects.create(
            author=telegram_user, movie=validated_data.pop("movie"), **validated_data
        )
        return instance


class ReviewRepresentationSerializer(serializers.ModelSerializer):
    """Representation serializer for 'Review' model."""

    author = serializers.SerializerMethodField()
    movie_title = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = [
            "id",
            "author",
            "movie_title",
            "text",
            "rating",
        ]

    def get_author(self, obj):
        username = obj.author.profile.username
        return username

    def get_movie_title(self, obj):
        title = obj.movie.title
        return title


class ReviewUpdateSerializer(ReviewRepresentationSerializer):

    class Meta:
        model = Review
        fields = [
            "id",
            "author",
            "movie_title",
            "text",
            "rating",
        ]
        read_only_fields = [
            "author",
            "movie_title",
        ]
