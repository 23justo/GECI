# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-22 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinica', '0002_clinica_moneda'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinica',
            name='color_footer',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clinica',
            name='color_menu',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clinica',
            name='color_texto_menu',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
