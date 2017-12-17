# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_auto_20170119_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='lifeInsurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_life_Insurance', models.CharField(max_length=100)),
                ('description_life_Insurance', models.TextField()),
                ('date_life', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='propertyInsurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_property_Insurance', models.CharField(max_length=100)),
                ('description_property_Insurance', models.TextField()),
                ('date_property', models.DateTimeField()),
            ],
        ),
    ]
