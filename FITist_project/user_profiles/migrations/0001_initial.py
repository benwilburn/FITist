# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 20:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workout_programs', '0014_auto_20170323_0225'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=255)),
                ('goal', models.CharField(choices=[('BM', 'Build Muscle'), ('LF', 'Lose Fat'), ('FT', 'Full Transformation')], default='LF', max_length=255)),
                ('experience', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced')], default='B', max_length=255)),
                ('length', models.CharField(choices=[('1M', '1 Month'), ('3M', '3 Month'), ('6M', '6 Month')], default='1M', max_length=255)),
                ('per_week', models.CharField(choices=[('2-3', '2-3 Days/Week'), ('4-5', '4-5 Days/Week'), ('6-7', '6-7 Days/Week')], default='2-3', max_length=255)),
                ('equipment_available', models.CharField(choices=[('None', 'No Equipment'), ('DB', 'Dumbbells'), ('FW', 'Free Weights'), ('M', 'Machines'), ('CE', 'Cardio Equipment'), ('KB', 'Kettlebells')], default='None', max_length=255)),
                ('program_selected', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='workout_programs.Program')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
