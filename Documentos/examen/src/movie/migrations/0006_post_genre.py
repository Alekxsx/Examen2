# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-17 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_remove_post_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('M', 'Mature'), ('A', 'Paratodos'), ('B', 'Adolecentes')], default='M', max_length=120),
        ),
    ]
