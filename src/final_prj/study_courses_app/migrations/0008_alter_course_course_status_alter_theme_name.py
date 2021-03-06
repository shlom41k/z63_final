# Generated by Django 4.0.3 on 2022-04-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_courses_app', '0007_alter_lesson_order_alter_theme_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_status',
            field=models.CharField(choices=[('Completed', 'COMPLETED'), ('In Process', 'IN_PROCESS')], default='In Process', max_length=20, verbose_name='Course Status'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Name'),
        ),
    ]
