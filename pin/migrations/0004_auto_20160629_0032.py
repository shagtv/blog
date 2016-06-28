# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 21:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0003_auto_20160629_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='activated',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='pin',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]