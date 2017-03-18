# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-11 04:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170306_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='/assets/images/no-img.jpg', upload_to='/assets/images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 11, 4, 13, 5, 267318)),
        ),
    ]