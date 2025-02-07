from django.db import models


class DirectorAbstract(models.Model):
    """Abstract model for director and actor models"""

    first_name = models.CharField(verbose_name="First Name", max_length=50)
    second_name = models.CharField(
        verbose_name="Middle Name", max_length=50, blank=True
    )
    last_name = models.CharField(verbose_name="Last Name", max_length=50)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.second_name[:1]}"

    class Meta:
        abstract = True
        unique_together = (
            "first_name",
            "second_name",
            "last_name",
        )


class Director(DirectorAbstract):
    """Director model"""

    pass
