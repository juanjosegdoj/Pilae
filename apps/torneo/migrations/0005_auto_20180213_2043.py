# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-14 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0004_auto_20171130_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneo',
            name='deporte',
            field=models.CharField(default='Baloncesto', max_length=25),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='nombre',
            field=models.CharField(default='---', max_length=70),
        ),
    ]