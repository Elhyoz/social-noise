# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_auto_20170104_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='musical_gender',
            field=models.CharField(max_length=90, null=True),
        ),
    ]
