# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clinica', '0001_initial'),
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='clinica',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Clinica.Clinica'),
            preserve_default=False,
        ),
    ]
