# Generated by Django 4.0.3 on 2022-04-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0007_alter_schoolcourseapplication_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolcourseapplication',
            name='status',
            field=models.CharField(choices=[('OPENED', 'Opened'), ('IN_WORK', 'In Work'), ('CLOSED', 'Closed')], default='OPENED', max_length=10, verbose_name='Status'),
        ),
    ]
