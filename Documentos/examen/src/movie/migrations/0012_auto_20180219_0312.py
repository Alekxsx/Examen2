# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-19 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_auto_20180219_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('T', 'Terror'), ('C', 'Ciencia ficcion'), ('F', 'Fantasia'), ('A', 'Accion')], default='M', max_length=120),
        ),
    ]
