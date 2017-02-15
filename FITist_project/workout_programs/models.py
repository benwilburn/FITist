from django.db import models


class WorkoutProgram(models.Model):
    """Program that customers pay for."""

    name = models.CharField(max_length=255)
    image = models.FileField()

    def __str__(self):
        """Will return Workout Program name for query set description."""
        return self.name
