# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-12 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rafflie', '0019_auto_20170211_0410'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='logo',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
