# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-12 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_auto_20181011_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
