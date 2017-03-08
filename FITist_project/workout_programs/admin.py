from django.contrib import admin
from workout_programs.models import ExerciseBlock
from workout_programs.models import ExerciseGroup
from workout_programs.models import Program
from workout_programs.models import ProgramTag
from workout_programs.models import Workout

admin.site.register(ProgramTag)


class ExerciseBlockInline(admin.StackedInline):
    """Extends form under program for exercise block in admin."""

    model = ExerciseBlock


class ExerciseGroupInline(admin.StackedInline):
    """Extends form under program for exercise group in admin."""

    model = ExerciseGroup


class WorkoutInline(admin.StackedInline):
    """Extemds form under program for workout in admin."""

    model = Workout


class ProgramAdmin(admin.ModelAdmin):
    """Program base form that extends for each inline."""

    inlines = [ExerciseBlockInline, ExerciseGroupInline, WorkoutInline, ]
