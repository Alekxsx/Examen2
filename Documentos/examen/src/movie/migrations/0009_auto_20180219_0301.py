# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-19 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_auto_20180219_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='Nombre', error_messages={'unique': 'Este titulo no es unico, intenta de nuevo'}, help_text='Debe ser un titulo unico', max_length=121, unique=True, verbose_name='Post'),
        ),
    ]