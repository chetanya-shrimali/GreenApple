# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-15 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20171114_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='message',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='customer name', max_length=50),
        ),
    ]