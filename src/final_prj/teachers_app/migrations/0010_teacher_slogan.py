# Generated by Django 4.0.3 on 2022-04-22 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers_app', '0009_alter_teacher_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='slogan',
            field=models.TextField(blank=True, max_length=300, verbose_name='Slogan'),
        ),
    ]