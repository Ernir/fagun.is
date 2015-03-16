# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('published_at', models.DateField()),
                ('slug', models.SlugField()),
                ('main_text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
