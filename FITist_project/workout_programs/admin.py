from django.contrib import admin
from workout_programs.models import ExerciseBlock
from workout_programs.models import ExerciseGroup
from workout_programs.models import Measurement
from workout_programs.models import MeasurementType
from workout_programs.models import Program
from workout_programs.models import Set
from workout_programs.models import Workout

admin.site.register(Program)
admin.site.register(Workout)
admin.site.register(ExerciseGroup)
admin.site.register(ExerciseBlock)
admin.site.register(MeasurementType)
admin.site.register(Measurement)
admin.site.register(Set)
