# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-29 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170829_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtime',
            name='code',
            field=models.CharField(default='2565b286', help_text='절대 수정하지 마세요!!', max_length=10, verbose_name='수업 코드 (수정금지)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='joined_classes',
            field=models.ManyToManyField(blank=True, related_name='joined_class', to='core.ClassTime', verbose_name='수강 수업'),
        ),
    ]