# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-26 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('A1', models.CharField(max_length=200)),
                ('A2', models.CharField(max_length=200)),
                ('A3', models.CharField(max_length=200)),
                ('A4', models.CharField(max_length=200)),
            ],
        ),
    ]
