# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-19 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo_solicitante', models.EmailField(max_length=254)),
                ('nombre_completo', models.CharField(max_length=250)),
                ('tema', models.CharField(max_length=250)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]
