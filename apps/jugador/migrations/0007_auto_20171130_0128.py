# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-30 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugador', '0006_auto_20171130_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='sexo',
            field=models.CharField(choices=[('MAS', 'Masculino'), ('FEM', 'Femenino')], max_length=3),
        ),
    ]
