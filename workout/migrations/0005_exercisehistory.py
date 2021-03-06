# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 23:48
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import workout.models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0004_auto_20170118_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('sets', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=10), default=[], size=10)),
                ('set_weights', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=10), default=[], size=10)),
                ('notes', models.TextField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='workout.Exercise')),
            ],
            bases=(models.Model, workout.models.ModelMixin),
        ),
    ]
