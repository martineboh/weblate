# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-24 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20161021_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dashboard_view',
            field=models.IntegerField(choices=[(1, 'Watched translations'), (2, 'Your languages'), (4, 'Component list'), (5, 'Suggested translations')], default=1, verbose_name='Default dashboard view'),
        ),
    ]
