# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_programs', '0010_program_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='tags',
        ),
        migrations.AddField(
            model_name='programtag',
            name='related_programs',
            field=models.ManyToManyField(related_name='tags', to='workout_programs.Program'),
        ),
    ]