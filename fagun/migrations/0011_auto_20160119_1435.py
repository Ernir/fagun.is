# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 14:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fagun', '0010_auto_20160119_1325'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsArticle',
            new_name='NewsStory',
        ),
        migrations.AlterModelOptions(
            name='educationalarticle',
            options={'ordering': ('-published_at',)},
        ),
    ]
