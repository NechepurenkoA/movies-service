# Generated by Django 5.1.5 on 2025-02-06 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("directors", "0002_alter_director_second_name"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="director",
            unique_together={("first_name", "second_name", "last_name")},
        ),
    ]
