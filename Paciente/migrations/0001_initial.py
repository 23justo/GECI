# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 06:56
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
                ('nombres', models.CharField(max_length=250)),
                ('apellidos', models.CharField(max_length=250)),
                ('sexo', models.CharField(choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre')], max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('tipo_sangre', models.CharField(choices=[('A Positiva', 'A Positiva'), ('A Negativo', 'A Negativo'), ('B Positivo', 'B Positivo'), ('B Negativo', 'B Negativo'), ('O Positivo', 'O Positivo'), ('AB Positivo', 'AB Positivo'), ('AB Negativo', 'AB Negativo')], max_length=15)),
                ('telefono_casa', models.CharField(max_length=15)),
                ('telefono_personal', models.CharField(max_length=15)),
                ('dpi', models.CharField(max_length=40)),
                ('seguro', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
