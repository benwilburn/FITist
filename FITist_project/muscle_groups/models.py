from django.db import models
from exercises.models import Exercise


class MuscleGroup(models.Model):
    """Muscle group used for an exercise."""

    name = models.CharField(max_length=255, default='')
    associated_lifts = models.ManyToManyField(
        Exercise,
        related_name='muscles_used')

    def __str__(self):
        """Will return muscle group name as query object description."""
        return self.name
