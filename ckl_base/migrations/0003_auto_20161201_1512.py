# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckl_base', '0002_auto_20161114_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='outlet',
            name='name',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
