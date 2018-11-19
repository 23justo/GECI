# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-18 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0005_usuario_modulo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='modulo_citas',
            field=models.IntegerField(choices=[('Lectura', 1), ('Escritura', 2), ('Eliminacion', 3), ('Todos', 4)]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='modulo_contable',
            field=models.IntegerField(choices=[('Lectura', 1), ('Escritura', 2), ('Eliminacion', 3), ('Todos', 4)]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='modulo_doctor',
            field=models.IntegerField(choices=[('Lectura', 1), ('Escritura', 2), ('Eliminacion', 3), ('Todos', 4)]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='modulo_paciente',
            field=models.IntegerField(choices=[('Lectura', 1), ('Escritura', 2), ('Eliminacion', 3), ('Todos', 4)]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='modulo_secretaria',
            field=models.IntegerField(choices=[('Lectura', 1), ('Escritura', 2), ('Eliminacion', 3), ('Todos', 4)]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='modulo_usuario',
            field=models.IntegerField(choices=[('Lectura', 1), ('Escritura', 2), ('Eliminacion', 3), ('Todos', 4)]),
        ),
    ]