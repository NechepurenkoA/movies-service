# Generated by Django 5.1.2 on 2025-02-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("directors", "0001_initial"),
        ("movies", "0003_alter_movie_genre"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="directors",
            field=models.ManyToManyField(default="Unknown", to="directors.director"),
        ),
        migrations.DeleteModel(
            name="MovieDirector",
        ),
    ]
