# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-17 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import movie.validators


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_post_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='studio',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[movie.validators.validate_studio]),
        ),
    ]