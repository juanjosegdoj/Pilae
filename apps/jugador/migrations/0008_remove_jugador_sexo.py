# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-30 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jugador', '0007_auto_20171130_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='sexo',
        ),
    ]
