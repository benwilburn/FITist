"""Models for workouts."""
from django.db import models
from django.shortcuts import get_object_or_404
from exercise_library.models import Exercise
from questions.models import Answer


class Program(models.Model):
    """Program that customers pay for."""

    name = models.CharField(max_length=255)
    total_weeks = models.IntegerField(default=1)
    tags = models.ManyToManyField(Answer, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        """Will return Workout Program name for query set description."""
        return "{}".format(self.name)


class Workout(models.Model):
    """A week(and program) can have multiple workouts."""

    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    week_number = models.IntegerField(default=1)
    program = models.ForeignKey(Program)
    tags = models.ManyToManyField(Answer)
    completed = models.BooleanField(default=False)

    def __str__(self):
        """Will return the name of the workout as query set description."""
        return self.name


class ExerciseGroup(models.Model):
    """Exercise blocks can be grouped together to form a superset."""

    description = models.TextField()
    order = models.IntegerField(default=0)
    workout_group_belongs_to = models.ForeignKey(
        Workout,
        related_name='assocated_exercise_groups')

    class Meta(object):
        """Orders each group based on the order number assigned."""

        ordering = ['order', ]

    def __str__(self):
        """Will return the description of the grouping of exercises."""
        return "description: {}, order: {}".format(
            self.description,
            self.order)


class ExerciseBlock(models.Model):
    """Each workout will have multiple blocks of exercise.

    Each exercise block can have multiple exercises.
    """

    exercise = models.ForeignKey(Exercise)
    order = models.IntegerField(default=0, blank=True)
    assigned_group = models.ForeignKey(
        ExerciseGroup,
        related_name='associated_exercise_blocks')
    prescription = models.TextField(
        default="no prescription has been written yet")

    class Meta(object):
        """Orders each exercise by Exercse.exercise_priorty."""

        ordering = ['exercise', 'order', ]

    def __str__(self):
        """Will return the name of the exercise in the block."""
        return self.exercise.name


def get_program_instance(program_pk):
    return get_object_or_404(Program, pk=program_pk)
