# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-30 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugador', '0009_jugador_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='apellidos',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='nombres',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
    ]