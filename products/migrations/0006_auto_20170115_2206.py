# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 22:06
from __future__ import unicode_literals

from django.db import migrations

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20170115_2152'),
    ]

    operations = [
	migrations.CreateModel('ProductPhoto', fields=[
                ('photo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Photo')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            bases=('products.photo',),
        ),
    ]