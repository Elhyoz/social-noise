# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Musician',
        ),
        migrations.AddField(
            model_name='artist',
            name='instrument',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
