# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 08:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0002_auto_20160619_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='is_owner',
        ),
    ]
