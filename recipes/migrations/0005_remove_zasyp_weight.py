# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-22 20:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20161217_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zasyp',
            name='weight',
        ),
    ]
