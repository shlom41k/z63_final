# Generated by Django 4.0.3 on 2022-04-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers_app', '0007_alter_teacher_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Slug'),
        ),
    ]