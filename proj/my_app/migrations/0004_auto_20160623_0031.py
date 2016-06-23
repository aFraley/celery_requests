# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20160621_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='tweet_favorite_cnt',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_retweet_cnt',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_source',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]