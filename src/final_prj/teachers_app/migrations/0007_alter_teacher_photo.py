# Generated by Django 4.0.3 on 2022-04-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers_app', '0006_alter_teacher_detail_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(upload_to='school_teachers/', verbose_name='Photo'),
        ),
    ]
