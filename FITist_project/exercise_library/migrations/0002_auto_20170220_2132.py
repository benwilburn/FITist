# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='exercise_limit',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='type',
            name='type_priority',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
