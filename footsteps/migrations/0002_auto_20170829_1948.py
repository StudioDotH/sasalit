# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-29 10:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20170829_1948'),
        ('footsteps', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '게시물', 'verbose_name_plural': '게시물'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='class_no',
        ),
        migrations.AddField(
            model_name='post',
            name='parent_class',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='post_class', to='core.ClassTime', verbose_name='수업'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_footsteps', to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AlterField(
            model_name='post',
            name='class_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='수업 날짜'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성 시간'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, verbose_name='제목'),
        ),
    ]
