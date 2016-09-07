# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20160905_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='bottled_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='foto',
            field=models.ImageField(upload_to='static/pictures/'),
        ),
    ]
