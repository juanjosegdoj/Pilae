# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-14 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0005_auto_20180213_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneo',
            name='nombre',
            field=models.CharField(default='', max_length=70),
        ),
    ]
