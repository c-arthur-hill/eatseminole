# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170115_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]
