# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0004_auto_20171215_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleInsurance', models.CharField(max_length=100)),
                ('descriptionInsurance', models.TextField()),
                ('insurance_type', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(default=None, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Insurance',
        ),
    ]