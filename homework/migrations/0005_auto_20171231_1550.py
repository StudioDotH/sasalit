# Generated by Django 2.0 on 2017-12-31 06:50

from django.db import migrations, models
import homework.models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0004_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='hw_file',
            field=models.FileField(null=True, upload_to=homework.models.get_file_path, verbose_name='과제물 파일'),
        ),
    ]