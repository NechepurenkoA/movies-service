# Generated by Django 5.1.5 on 2025-02-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0007_alter_movie_genre"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="image",
            field=models.ImageField(
                default="movies_previews/decoy.png",
                upload_to="movies_previews",
                verbose_name="Image",
            ),
        ),
    ]
