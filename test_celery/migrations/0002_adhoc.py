# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_celery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adhoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=128)),
                ('first', models.CharField(max_length=128)),
                ('second', models.CharField(max_length=128)),
                ('log_date', models.DateTimeField()),
            ],
        ),
    ]
