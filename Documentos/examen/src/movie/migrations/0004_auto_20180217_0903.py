# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-17 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20180217_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(max_length=120, verbose_name=(('M', 'Mature'), ('A', 'Paratodos'), ('B', 'Adolecentes'))),
        ),
    ]