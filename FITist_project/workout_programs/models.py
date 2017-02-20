from django.db import models

from exercise_library.models import Exercise


class Program(models.Model):
    """Program that customers pay for."""

    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        """Will return Workout Program name for query set description."""
        return self.name


class Workout(models.Model):
    """A week(and program) can have multiple workouts."""

    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    week_number = models.IntegerField()
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
    order = models.IntegerField(defaut=0, blank=True)
    assigned_group = models.ForeignKey(
        ExerciseGroup,
        related_name='associated_exercise_blocks')

    class Meta(object):
        """Orders each exercise by exercse.exercise_priorty."""

        ordering = ['exercise.exercise_priority', 'order', ]

    def __str__(self):
        """Will return the name of the exercise in the block."""
        return self.exercise['name']


class MeasurementType(models.Model):
    """Can be many types of measurements."""

    name = models.CharField(max_length=255)


class Measurement(models.Model):
    """Each exercise block needs a measurement."""

    description = models.TextField()
    number = models.IntegerField()
    measurement_type = models.ForeignKey(MeasurementType)


class Set(models.Model):
    number = models.IntegerField(default=0)
    set_order = models.IntegerField(default=0, blank=True, null=True)
    exercise_block = models.ForeignKey(ExerciseBlock)
#
#
# class Rep(Measurement):
#     number = models.IntegerField(default=0)
#     rep_order = models.IntegerFeild(default=0, blank=True, null=True)
#     exercise_block = models.ForeignKey(ExerciseBlock, blank=True, null=True)
#     set_which_work_should_be_performed = models.ForeignKey(
#         Set)
#
#
# class Duration(Measurement):
#     time = models.DurationField()
#     exercise_block = models.ForeignKey(ExerciseBlock, blank=True, null=True)
#     set_which_work_should_be_performed = models.ForeignKey(
#         Sets)
