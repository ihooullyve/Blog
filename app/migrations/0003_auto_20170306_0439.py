# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-06 04:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170306_0423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='text',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 6, 4, 39, 53, 194242)),
        ),
    ]
