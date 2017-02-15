from django.db import models


class Type(models.Model):
    """Specifies a type for an Exercise."""

    name = models.CharField(max_length=255)
    set_range = models.CharField(max_length=255, blank=True)
    rep_range = models.CharField(max_length=255, blank=True)
    percentage_range = models.CharField(max_length=255, blank=True)
    rest_time = models.DurationField(blank=True, null=True)
    exercise_limit = models.IntegerField(default=0)
    type_priority = models.IntegerField(default=0)

    def __str__(self):
        """Will return type name as query object description."""
        return self.name


class Exercise(models.Model):
    """Model for each possible exercise for a program."""

    name = models.CharField(max_length=255,)
    description = models.TextField()
    exercise_type = models.ManyToManyField(
        Type,
        related_name='associated_lifts',)
    exercise_priority = models.IntegerField(default=0, blank=True)
    video = models.FileField(blank=True, null=True)

    def __str__(self):
        """Will return exercise name as query object description."""
        return self.name
