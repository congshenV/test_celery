# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 22:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_celery', '0004_delete_ansible_beat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Add',
        ),
    ]
