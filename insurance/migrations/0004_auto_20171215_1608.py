# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_lifeinsurance_propertyinsurance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleInsurance', models.CharField(max_length=100)),
                ('descriptionInsurance', models.TextField()),
                ('insurance_type', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='autoInsurance',
        ),
        migrations.DeleteModel(
            name='lifeInsurance',
        ),
        migrations.DeleteModel(
            name='propertyInsurance',
        ),
    ]