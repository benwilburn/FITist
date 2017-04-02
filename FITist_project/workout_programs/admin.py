from django.contrib import admin
from workout_programs.models import ExerciseBlock
from workout_programs.models import ExerciseGroup
from workout_programs.models import Program
from workout_programs.models import Workout


class ExerciseBlockInline(admin.StackedInline):
    """Extends form under program for exercise block in admin."""

    model = ExerciseBlock
    extra = 1


class ExerciseGroupInline(admin.StackedInline):
    """Extends form under program for exercise group in admin."""

    model = ExerciseGroup
    extra = 4


class WorkoutInline(admin.StackedInline):
    """Extends form under program for workout in admin."""

    model = Workout
    extra = 2


class ProgramAdmin(admin.ModelAdmin):
    """Program base form that extends for each inline."""

    inlines = [WorkoutInline, ]


class WorkoutAdmin(admin.ModelAdmin):
    inlines = [ExerciseGroupInline, ]


class ExerciseGroupAdmin(admin.ModelAdmin):
    inlines = [ExerciseBlockInline, ]


admin.site.register(Program, ProgramAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(ExerciseGroup, ExerciseGroupAdmin)
admin.site.register(ExerciseBlock)
