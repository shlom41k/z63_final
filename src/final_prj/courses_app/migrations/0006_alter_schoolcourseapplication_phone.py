# Generated by Django 4.0.3 on 2022-04-19 11:01

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0005_schoolcourseapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolcourseapplication',
            name='phone',
            field=phone_field.models.PhoneField(max_length=31, verbose_name='Person Phone'),
        ),
    ]
