# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fagun', '0008_auto_20160119_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='fagun.Tag'),
        ),
    ]
