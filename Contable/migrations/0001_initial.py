# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clinica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovimientoCita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField()),
                ('pagado', models.BooleanField()),
                ('creado', models.DateTimeField(auto_now=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinica.Clinica')),
            ],
        ),
    ]
