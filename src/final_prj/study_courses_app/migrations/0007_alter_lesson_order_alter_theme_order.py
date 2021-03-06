# Generated by Django 4.0.3 on 2022-04-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_courses_app', '0006_alter_module_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='order',
            field=models.PositiveIntegerField(blank=True, verbose_name='Lesson Order'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='order',
            field=models.PositiveIntegerField(blank=True, verbose_name='Theme Order'),
        ),
    ]
