# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_bookmark_new_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]