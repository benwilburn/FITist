from django.db import models
from django.contrib.auth.models import User
from workout_programs.models import Program


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    program_selected = models.ForeignKey(Program, null=True)
    birth_day = models.DateField(null=True, blank=True)

    def __str__(self):
        """Will return User object str for query set description."""
        return "{}".format(self.user)

    def get_absolute_url(self):
        return "/user_profiles/{}".format(self.user.username)
