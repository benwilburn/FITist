from django.db import models

from exercise_library.models import Exercise


class Program(models.Model):
    """Program that customers pay for."""

    name = models.CharField(max_length=255)
    total_weeks = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)

    def __str__(self):
        """Will return Workout Program name for query set description."""
        return self.name


class Workout(models.Model):
    """A week(and program) can have multiple workouts."""

    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    week_number = models.IntegerField(default=1)
    program = models.ForeignKey(Program)
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

    class Meta(object):
        """Orders each exercise by Exercse.exercise_priorty."""

        ordering = ['exercise', 'order', ]

    def __str__(self):
        """Will return the name of the exercise in the block."""
        return self.exercise.name


class MeasurementType(models.Model):
    """Can have many types of measurements."""

    name = models.CharField(max_length=255)

    def __str__(self):
        """Will return measurement type name as query set description."""
        return self.name


class Measurement(models.Model):
    """Each exercise block needs a measurement."""

    number = models.IntegerField()
    measurement_type = models.ForeignKey(MeasurementType)

    def __str__(self):
        """Will return measurement description for query set description."""
        return "{}, {}".format(self.measurement_type.name, self.number)


class Set(models.Model):
    """Each exercise block will have a set or sets."""

    set_order = models.IntegerField(default=0, blank=True, null=True)
    exercise_block = models.ForeignKey(
        ExerciseBlock,
        related_name='sets_to_be_completed')
    measurement = models.ManyToManyField(Measurement)

    def __str__(self):
        """Returns set number & ExerciseBlock name as query set description."""
        return "{}, set_order: {}".format(
            self.exercise_block.exercise.name,
            self.set_order)
