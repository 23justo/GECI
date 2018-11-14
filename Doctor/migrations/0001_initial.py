# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-14 04:23
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
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=75)),
                ('apellidos', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=25)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=20)),
                ('especialidad', models.CharField(max_length=75)),
                ('direccion_clinica', models.CharField(max_length=150)),
                ('dpi', models.CharField(max_length=20)),
                ('clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinica.Clinica')),
            ],
        ),
    ]
