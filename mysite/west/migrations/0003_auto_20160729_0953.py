# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 01:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('west', '0002_sp_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Character',
            new_name='charname',
        ),
        migrations.DeleteModel(
            name='sp_name',
        ),
    ]
