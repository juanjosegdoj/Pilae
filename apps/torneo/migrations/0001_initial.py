# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-30 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='', max_length=25)),
                ('fecha', models.DateField()),
                ('sexo', models.CharField(choices=[('MAS', 'Masculino'), ('FEM', 'Femenino')], max_length=3)),
            ],
        ),
    ]
