# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 07:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rafflie', '0015_user_last_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 18, 7, 12, 54, 405946, tzinfo=utc)),
        ),
    ]
