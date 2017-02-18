# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_library', '0002_auto_20170215_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='exercise_limit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='type',
            name='percentage_range',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='type',
            name='rep_range',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='type',
            name='rest_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='type',
            name='set_range',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='type',
            name='type_priority',
            field=models.IntegerField(default=0),
        ),
    ]
