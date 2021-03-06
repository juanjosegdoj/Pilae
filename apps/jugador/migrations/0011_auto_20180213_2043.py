# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-14 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugador', '0010_auto_20171130_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='apellidos',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='domicilio',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='email',
            field=models.EmailField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='nombres',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='telefono',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
