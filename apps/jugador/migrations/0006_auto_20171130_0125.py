# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-30 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugador', '0005_auto_20171130_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='nombre',
        ),
        migrations.AddField(
            model_name='jugador',
            name='apellidos',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='jugador',
            name='nombres',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='sexo',
            field=models.CharField(choices=[('MAS', 'Masculino'), ('FEM', 'Femenino')], default='MAS', max_length=3),
        ),
    ]