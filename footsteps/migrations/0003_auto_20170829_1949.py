# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-29 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('footsteps', '0002_auto_20170829_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='class_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='수업 날짜'),
        ),
    ]
