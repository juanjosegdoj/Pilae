# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-14 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0004_auto_20180116_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='id',
        ),
        migrations.AlterField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(max_length=35, primary_key=True, serialize=False),
        ),
    ]