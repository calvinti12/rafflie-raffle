# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-16 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rafflie', '0021_auto_20170211_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raffle',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
