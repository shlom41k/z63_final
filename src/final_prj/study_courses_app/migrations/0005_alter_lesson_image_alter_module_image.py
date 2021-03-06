# Generated by Django 4.0.3 on 2022-04-13 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_courses_app', '0004_alter_lesson_image_alter_module_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(blank=True, upload_to='courses/modules/lessons/', verbose_name='Module Image'),
        ),
        migrations.AlterField(
            model_name='module',
            name='image',
            field=models.ImageField(blank=True, upload_to='courses/modules/', verbose_name='Module Image'),
        ),
    ]
