# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rafflie', '0005_auto_20161222_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]