# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 22:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0008_exercise_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='exercise_name',
            new_name='name',
        ),
    ]