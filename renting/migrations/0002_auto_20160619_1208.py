# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=60)),
                ('is_owner', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='country',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='myuser',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='renting.MyUser'),
        ),
    ]
