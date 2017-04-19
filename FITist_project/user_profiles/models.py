from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from workout_programs.models import Program


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    program_selected = models.ForeignKey(Program, null=True)
    birth_day = models.DateField(null=True, blank=True)

    def __str__(self):
        """Will return User object str for query set description."""
        return "{}".format(self.user)


def create_user_profile(user, program):
        Profile.objects.create(
            user=user,
            program_selected=program
        )


@receiver(pre_save, sender=User)
def set_user_password(sender, instance, *args, **kwargs):
    instance.set_password(instance.password)
