# Generated by Django 4.0.3 on 2022-04-10 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0002_rename_course_schoolcourse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolcourse',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=100, unique=True, verbose_name='Slug'),
        ),
    ]
