# Generated by Django 4.0.3 on 2022-04-07 19:03

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers_app', '0004_teacher_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='detail_info',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Detail Info'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='short_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='Photo'),
        ),
    ]