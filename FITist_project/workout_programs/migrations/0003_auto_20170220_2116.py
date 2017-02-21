# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_programs', '0002_program_total_weeks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='total_weeks',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='workout',
            name='week_number',
            field=models.IntegerField(default=1),
        ),
    ]