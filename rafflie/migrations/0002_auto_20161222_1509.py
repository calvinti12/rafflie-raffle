# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 15:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rafflie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaffleMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2016, 12, 22, 15, 9, 4, 67523, tzinfo=utc), verbose_name='date created')),
            ],
        ),
        migrations.RemoveField(
            model_name='owner',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='raffle',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='owner',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 15, 9, 4, 86144, tzinfo=utc), verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='product',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 15, 9, 4, 87058, tzinfo=utc), verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='raffle',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 15, 9, 4, 87865, tzinfo=utc), verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 15, 9, 4, 88636, tzinfo=utc), verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 15, 9, 4, 85320, tzinfo=utc), verbose_name='date created'),
        ),
    ]
