# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout_programs', '0003_auto_20170220_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkTime',
            fields=[
                ('measurement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='workout_programs.Measurement')),
                ('duration', models.DurationField()),
            ],
            bases=('workout_programs.measurement',),
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='description',
        ),
    ]
