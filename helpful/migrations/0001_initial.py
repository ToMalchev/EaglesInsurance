# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-17 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='helpful',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=60)),
                ('text', models.TextField(default='')),
                ('model_pic', models.ImageField(default='static/personal/img/New Logo Black.jpg', upload_to='pic_folder/')),
            ],
        ),
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(default='', max_length=60)),
                ('text', models.TextField(default='')),
            ],
        ),
    ]
