# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 11:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpful', '0003_helpful_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helpful',
            name='model_pic',
        ),
    ]
