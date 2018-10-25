# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-15 03:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Paciente', '0003_auto_20181008_0914'),
        ('Cita', '0002_auto_20181014_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Paciente.Paciente'),
            preserve_default=False,
        ),
    ]
